from unittest import result
from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
import os
import uuid
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.security import OAuth2PasswordBearer

from db import get_session
from models import User

router = APIRouter()

# --- JWT Configuration ---
SECRET_KEY = os.getenv("BETTER_AUTH_SECRET", "fallback_test_secret_key_for_development")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# --- Pydantic Schemas ---
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

# --- Helper Functions ---
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# --- Routes ---

@router.post("/auth/register", response_model=UserResponse)
async def register(user: UserCreate, session: AsyncSession = Depends(get_session)):
        # 1. Check if user exists
        statement = select(User).where(User.email == user.email)
        result = await session.exec(statement) 
        existing_user = result.first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # 2. Create new user
        user_id = str(uuid.uuid4())
        db_user = User(
            id=user_id,
            email=user.email,
            name=user.name or user.email.split('@')[0]
        )
        
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user

@router.post("/auth/login", response_model=Token)
async def login(user: UserLogin, session: AsyncSession = Depends(get_session)):

        # 1. Find user by email
        statement = select(User).where(User.email == user.email)
        result = await session.exec(statement) # await lagaya
        db_user = result.first()
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Invalid email or password"
            )

        # 2. Generate Token with REAL DB ID
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": str(db_user.id), "email": db_user.email},
            expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer"}

@router.post("/auth/logout")
async def logout():
    # Since JWTs are stateless, logout can be handled on the client side by deleting the token.
    return {"message": "Logged out successfully"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    statement = select(User).where(User.id == user_id)
    result = await session.exec(statement)
    user = result.first()
    
    if user is None:
        raise credentials_exception
    return user