from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    """
        SQLAlchemy model representing a book in the database.

    Attributes:
        id (int): Primary key identifier.
        title (str): Book title, cannot be null.
        author (str): Book author, cannot be null.
        year (int): Year of publication, optional.
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True, default=None)
