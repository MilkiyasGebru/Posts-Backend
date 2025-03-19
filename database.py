from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine, text

import urllib.parse

password = ""
encoded_password = urllib.parse.quote_plus(password)


class Base(DeclarativeBase):
    pass


db_url = f"postgresql+psycopg2://postgres:{encoded_password}@localhost:5432/fastapi"

engine = create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


Base.metadata.create_all(engine)