import logging
import os

from config import database_url
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = os.environ['database_url']
SQLALCHEMY_DATABASE_URL = database_url
# "postgresql://postgres:newpassword@69.164.218.16/mytestdb"

# "postgresql://brendan:ol64hg0alqmk9av5@db-postgresql-nyc1-29754-do-user-7668124-0.b.db.ondigitalocean.com:25060/fastapi?sslmode=require"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
