from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db
from models import Book

# Create database tables
models.Base.metadata.create_all(bind=engine)

# FastAPI application
app = FastAPI(
    title="Book API",
    description="API for managing books",
    version="1.0.0",
)


# POST /books/ - Add new book
@app.post("/books/", response_model=schemas.BookResponse)
async def create_book(data: schemas.BookCreate, db: Session = Depends(get_db)) -> Book:
    """
    Create a new book in the database.

    Args:
        data (schemas.BookCreate): Book data including title, author, and optional year.
        db (Session): Database session dependency.

    Returns:
        schemas.BookResponse: Created book object with ID.

    Raises:
        HTTPException: If validation fails (handled by FastAPI).
    """
    book = models.Book(title=data.title, author=data.author, year=data.year)

    db.add(book)
    db.commit()
    db.refresh(book)

    return book


# GET /books/ - Get all books
@app.get("/books/", response_model=List[schemas.BookResponse])
async def get_books(db: Session = Depends(get_db)) -> list[type[Book]]:
    """
    Retrieve all books from the database.

    Args:
        db (Session): Database session dependency.

    Returns:
        List[schemas.BookResponse]: List of all book objects.
    """
    return db.query(models.Book).all()


# DELETE /books/{book_id} - Delete a book by ID
@app.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    """
    Delete a book by its ID.

    Args:
        book_id (int): ID of the book to delete.
        db (Session): Database session dependency.

    Returns:
        dict: Confirmation message.

    Raises:
        HTTPException: If book with given ID is not found.
    """
    book = db.query(models.Book).filter(book_id == models.Book.id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": f"Book with id {book_id} deleted successfully"}


# PUT /books/{book_id} - Update book details
@app.put("/books/{book_id}", response_model=schemas.BookResponse)
async def update_book(
    book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)
) -> type[Book]:
    """
    Update an existing book's details.

    Args:
        book_id (int): ID of the book to update.
        book_update (schemas.BookUpdate): Partial book data for update.
        db (Session): Database session dependency.

    Returns:
        schemas.BookResponse: Updated book object.

    Raises:
        HTTPException: If book with given ID is not found.
    """

    book = db.query(models.Book).filter(book_id == models.Book.id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    # Update only provided fields (partial update)
    update_data = book_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)
    return book


# GET /books/ - Search book by title, author, or year
@app.get("/books/search/", response_model=List[schemas.BookResponse])
async def search_books(
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[int] = None,
    db: Session = Depends(get_db),
) -> list[type[Book]]:
    """
    Search books by title, author, or year.

    Args:
        title (Optional[str]): Title substring to search for.
        author (Optional[str]): Author substring to search for.
        year (Optional[int]): Exact year to search for.
        db (Session): Database session dependency.

    Returns:
        List[schemas.BookResponse]: List of books matching the search criteria.
    """
    if not any([title, author, year is not None]):
        return []

    query = db.query(models.Book)

    # Apply filters if parameters are provided
    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(year == models.Book.year)

    return query.all()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
