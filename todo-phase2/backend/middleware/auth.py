from fastapi import HTTPException, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from typing import Optional
import os

security = HTTPBearer()

def verify_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """
    Verify JWT token and extract user_id
    """
    token = credentials.credentials
    secret = os.getenv("BETTER_AUTH_SECRET", "fallback_test_secret_key_for_development")  # Same fallback as auth routes

    if not secret:
        raise HTTPException(status_code=500, detail="Server configuration error: missing auth secret")

    try:
        # Decode the token
        payload = jwt.decode(token, secret, algorithms=["HS256"])

        # Extract user_id (assuming it's stored as 'sub' in the token)
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")

        return {"user_id": user_id}
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")


def validate_user_access(request: Request, token_data: dict = Depends(verify_jwt_token)) -> str:
    """
    Validate that the user_id in the URL matches the user_id in the JWT token
    """
    url_user_id = request.path_params.get("user_id")
    token_user_id = token_data.get("user_id")

    if url_user_id != token_user_id:
        raise HTTPException(
            status_code=403,
            detail="Access denied: cannot access other user's tasks"
        )

    return token_user_id