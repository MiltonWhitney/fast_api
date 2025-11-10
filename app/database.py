#app/database.py

# SQLAlchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orn import sessionmaker, declarative_base

# Database URL configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"

# Create the SQLalchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False}
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Creating a base class for declarative class definitions
Base = declarative_base()