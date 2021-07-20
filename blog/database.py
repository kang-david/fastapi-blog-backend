from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@postgresserver/db'
SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///./blog.db'

# connect_args flag only needed for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})


SessionLocal = sessionmaker(autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()