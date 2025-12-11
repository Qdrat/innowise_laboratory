from typing import Optional
from pydantic import BaseModel, Field


class BookBase(BaseModel):
    """
    Base schema for book data with common validation rules.
    """
    title: str = Field(
        min_length=1,
        max_length=200,
        description="The name of the book",
    )

    author: str = Field(
        min_length=1,
        max_length=100,
        description="The author of the book",
    )
    year: int | None = Field(
        None,
        ge=0,
        description="Year of publication",
    )



class BookCreate(BookBase):
    """
    Schema for creating a new book.
    All fields are required except year.
    """
    pass



class BookUpdate(BaseModel):
    """
    Schema for updating an existing book.
    All fields are optional for partial updates.
    """
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None



class BookResponse(BookBase):
    """
    Schema for returning book data in responses.
    Includes the database ID and supports ORM mode.
    """
    id: int
    title: str
    author: str
    year: Optional[int] = None

    class Config:
        """Pydantic configuration."""
        orm_mode = True
