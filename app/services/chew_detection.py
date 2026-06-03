import cv2
import mediapipe as mp
import math
import time
from sqlalchemy.orm import Session
from app.models.eating_session import EatingSession
from datetime import datetime

# MediaPipe Solutions
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def detect_chews(db: Session):
    cap = cv2.VideoCapture(0)
    
    chew_count = 0
    bite_count = 0
    mouth_open = False
    hand_near_mouth = False
    active_duration = 0.0  
    prev_frame_time = time.time()

    # Face Landmarks
    TOP_LIP, BOTTOM_LIP = 13, 14
    LEFT_MOUTH, RIGHT_MOUTH = 61, 291

    with mp_face_mesh.FaceMesh(refine_landmarks=True) as face_mesh, \
         mp_hands.Hands(min_detection_confidence=0.7) as hands:

        while cap.isOpened():
            success, frame = cap.read()
            if not success: break

            current_frame_time = time.time()
            delta_time = current_frame_time - prev_frame_time
            prev_frame_time = current_frame_time

            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            face_results = face_mesh.process(rgb_frame)
            hand_results = hands.process(rgb_frame)

            # 1. Chew Detection Logic
            if face_results.multi_face_landmarks:
                face_lm = face_results.multi_face_landmarks[0].landmark
                points = [(int(l.x * w), int(l.y * h)) for l in face_lm]

                v_dist = distance(points[TOP_LIP], points[BOTTOM_LIP])
                h_dist = distance(points[LEFT_MOUTH], points[RIGHT_MOUTH])
                
                if h_dist > 0:
                    mar = v_dist / h_dist
                    if mar > 0.08:
                        mouth_open = True
                        active_duration += delta_time
                    elif mouth_open and mar < 0.05:
                        chew_count += 1
                        mouth_open = False
                
                # 2. Bite Detection Logic (Hand tracking)
                if hand_results.multi_hand_landmarks:
                    hand_lm = hand_results.multi_hand_landmarks[0].landmark
                    mouth_center = ((face_lm[13].x + face_lm[14].x)/2, (face_lm[13].y + face_lm[14].y)/2)
                    index_tip = (hand_lm[8].x, hand_lm[8].y)
                    
                    dist = math.sqrt((mouth_center[0] - index_tip[0])**2 + (mouth_center[1] - index_tip[1])**2)
                    
                    if dist < 0.08: 
                        if not hand_near_mouth:
                            bite_count += 1
                            hand_near_mouth = True
                    else:
                        hand_near_mouth = False

            # UI Update: Rectangle and Text
            cv2.rectangle(frame, (10, 10), (350, 150), (0, 0, 0), -1)
            cv2.putText(frame, f"Chews: {chew_count}", (25, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            cv2.putText(frame, f"Bites: {bite_count}", (25, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
            cv2.putText(frame, f"Time: {active_duration:.1f}s", (25, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            cv2.imshow("ChewBe Monitoring", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"): break

    cap.release()
    cv2.destroyAllWindows()

    # --- DATABASE SAVE ---
    try:
        new_session = EatingSession(
            chew_count=chew_count,
            bite_count=bite_count,
            eating_speed=round(active_duration, 2),
            started_at=datetime.utcnow(),
            ended_at=datetime.utcnow()
        )
        db.add(new_session)
        db.commit()
    except Exception as e:
        db.rollback()

    return {
        "chew_count": chew_count,
        "bite_count": bite_count,
        "active_chew_duration": round(active_duration, 2)
    }