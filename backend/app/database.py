from sqlmodel import create_engine, Session, SQLModel
from app.config import settings
from app.models import User, Task


# Create the database engine
engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)


def create_db_and_tables():
    """Create all database tables defined in models"""
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("Tables created successfully")


def get_session():
    with Session(engine) as session:
        yield session