from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine, text

import urllib.parse

password = "Miki@0929054164"
encoded_password = urllib.parse.quote_plus(password)


class Base(DeclarativeBase):
    pass


db_url = f"postgresql+psycopg2://postgres:{encoded_password}@localhost:5432/fastapi"

engine = create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# with engine.connect() as conn:
#     create_table_statement = text("CREATE TABLE some_table (x int, y int)")
#     insert_data_statement = text("INSERT INTO some_table (x,y) VALUES (:x,:y)")
#     data = [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
#
#     conn.execute(create_table_statement)
#     conn.execute(insert_data_statement, data)
#     conn.commit()

Base.metadata.create_all(engine)
