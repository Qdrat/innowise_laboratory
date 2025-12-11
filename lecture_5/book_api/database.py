from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Database URL for SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.
    Provides a common base for declarative class definitions.
    """
    pass

# Session factory for creating database sessions
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db():
    """
    Dependency function to get database session.

    Yields:
        Session: SQLAlchemy database session.

    Raises:
        Exception: Any database error that occurs during the session.
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
