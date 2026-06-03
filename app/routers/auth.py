from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.utils.email import send_email
from app.utils.otp import generate_otp

from app.db.database import get_db

from app.models.user import User
from app.models.otp import OTPVerification

from app.schemas.auth import (
    UserRegister,
    UserLogin,
    VerifyOTP,
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    otp = generate_otp()

    otp_record = OTPVerification(
        user_id=new_user.id,
        otp=otp,
        purpose="verify_email",
        expires_at=datetime.utcnow() + timedelta(minutes=10)
    )

    db.add(otp_record)
    db.commit()

    send_email(
        new_user.email,
        "Email Verification",
        f"Your OTP is {otp}"
    )

    return {
        "message": "OTP sent successfully",
         "otp": otp
    }
@router.post("/verify-otp")
def verify_otp(
    data: VerifyOTP,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    otp_record = db.query(
        OTPVerification
    ).filter(
        OTPVerification.user_id == user.id,
        OTPVerification.otp == data.otp,
        OTPVerification.purpose == "verify_email"
    ).first()

    if not otp_record:
        raise HTTPException(
            status_code=400,
            detail="Invalid OTP"
        )

    # OTP EXPIRY CHECK
    if otp_record.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=400,
            detail="OTP expired"
        )

    user.is_verified = True

    db.commit()

    return {
        "message": "Email verified successfully"
    }

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    # EMAIL VERIFIED CHECK
    if not db_user.is_verified:
        raise HTTPException(
            status_code=403,
            detail="Email not verified"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": str(db_user.id)}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.post("/logout")
def logout():
    return {"message": "User logged out successfully"}