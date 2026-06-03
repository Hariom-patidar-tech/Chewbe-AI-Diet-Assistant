import cv2
import mediapipe as mp
import math
import time
from sqlalchemy.orm import Session
from app.models.eating_session import EatingSession
from datetime import datetime

# Mediapipe configuration
try:
    from mediapipe.python.solutions import face_mesh as mp_face_mesh
except ImportError:
    import mediapipe as mp
    mp_face_mesh = mp.solutions.face_mesh

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def detect_chews(db: Session):
    """
    Detects active chewing and SAVES data to database upon exit.
    """
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        return {"total_chews": 0, "active_chew_duration": 0, "error": "Camera error"}

    chew_count = 0
    mouth_open = False
    active_duration = 0.0  
    prev_frame_time = time.time()

    # Landmarks
    TOP_LIP, BOTTOM_LIP = 13, 14
    LEFT_MOUTH, RIGHT_MOUTH = 61, 291

    with mp_face_mesh.FaceMesh(
        max_num_faces=1, 
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as face_mesh:

        while cap.isOpened():
            success, frame = cap.read()
            if not success: break

            current_frame_time = time.time()
            delta_time = current_frame_time - prev_frame_time
            prev_frame_time = current_frame_time

            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb_frame)

            if results.multi_face_landmarks:
                face_landmarks = results.multi_face_landmarks[0]
                points = [(int(l.x * w), int(l.y * h)) for l in face_landmarks.landmark]

                v_dist = distance(points[TOP_LIP], points[BOTTOM_LIP])
                h_dist = distance(points[LEFT_MOUTH], points[RIGHT_MOUTH])
                
                if h_dist > 0:
                    mar = v_dist / h_dist
                    
                    # Logic: Sirf munh khulne par active time badhega
                    if mar > 0.08:
                        mouth_open = True
                        active_duration += delta_time
                    
                    elif mouth_open and mar < 0.05:
                        chew_count += 1
                        mouth_open = False

            # UI Update
            cv2.rectangle(frame, (10, 10), (320, 120), (0, 0, 0), -1)
            cv2.putText(frame, f"Chews: {chew_count}", (25, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.putText(frame, f"Active Time: {active_duration:.1f}s", (25, 100), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            cv2.imshow("ChewBe Monitoring", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()

    # --- DATABASE SAVE LOGIC ---
    try:
        new_session = EatingSession(
        chew_count=chew_count,
        eating_speed=round(active_duration, 2),
        started_at=datetime.utcnow(),
        ended_at=datetime.utcnow()
        )
        db.add(new_session)
        db.commit()
        db.refresh(new_session)
        
    except Exception as e:
        db.rollback()
        print(f"DATABASE ERROR: {str(e)}")

    return {
        "total_chews": chew_count,
        "active_chew_duration": round(active_duration, 2),
        "status": "Saved to DB"
    }