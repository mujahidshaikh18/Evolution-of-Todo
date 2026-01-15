from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
import os
import uuid

router = APIRouter()

# JWT configuration
SECRET_KEY = os.getenv("BETTER_AUTH_SECRET", "fallback_test_secret_key_for_development")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class UserCreate(BaseModel):
    email: str
    password: str
    name: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    id: str
    email: str
    name: Optional[str] = None

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/auth/register", response_model=UserResponse)
def register(user: UserCreate):
    """Register a new user (creates a user ID and returns it)"""
    # In this simplified implementation, we just generate a user ID
    # In a real system, you'd store user data in a database
    user_id = str(uuid.uuid4())

    new_user = UserResponse(
        id=user_id,
        email=user.email,
        name=user.name or user.email.split('@')[0]
    )

    return new_user

@router.post("/auth/login", response_model=Token)
def login(user: UserLogin):
    """Authenticate user and return JWT token"""
    # In this simplified implementation, we just validate the email format
    # In a real system, you'd verify the password against stored hash
    if not user.email or "@" not in user.email:
        raise HTTPException(status_code=401, detail="Invalid email format")

    # Generate a user ID for this user (in a real system, you'd look up the existing user)
    user_id = str(uuid.uuid4())

    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_id, "email": user.email},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/auth/logout")
def logout():
    """Simple logout endpoint (client-side token removal is sufficient)"""
    return {"message": "Logged out successfully"}