from datetime import timedelta, datetime, timezone

import jwt
from fastapi import HTTPException,status
from jwt import InvalidTokenError

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    data_tobe_encoded = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta

    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    data_tobe_encoded.update({"exp": expire})
    access_token = jwt.encode(data_tobe_encoded, SECRET_KEY, ALGORITHM)
    return access_token


def verify_token(token):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except InvalidTokenError:
        raise credentials_exception


print(create_access_token({"name": "Miki"}))
