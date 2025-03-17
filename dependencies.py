from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from utils.auth import verify_token
from database import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


async def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_db_session)):

    if not verify_token(token):

        raise HTTPException(401, "Invalid token")

    return {"user": "This is the user"}