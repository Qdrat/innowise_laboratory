from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from typing import List, Optional

import models
import schemas
from database import *


# создаем таблицы
models.Base.metadata.create_all(bind=engine)
# приложение, которое ничего не делает
app = FastAPI(
    title="Book API",
    description="API for managing books",
    version="1.0.0",
)

# POST /books/ - Add new book
@app.post("/books/", response_model=schemas.BookResponse)
async def create_book(data: schemas.BookCreate, db: Session = Depends(get_db)):
    book = models.Book(title = data.title, author = data.author, year = data.year)

    db.add(book)
    db.commit()
    db.refresh(book)
    return book

# GET /books/ - Get all books
@app.get("/books/", response_model=List[schemas.BookResponse])
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

# DELETE /books/{book_id} - Delete a book by ID
@app.delete("/books/{book_id}")
async def delete_book(book_id: int,
                      db: Session = Depends(get_db)):
    # Find book
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": f"Book with id {book_id} deleted successfully"}

# PUT /books/{book_id} - Update book details
@app.put("/books/{book_id}", response_model=schemas.BookResponse)
async def update_book(book_id: int,
                      book_update: schemas.BookUpdate,
                      db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(book_id == models.Book.id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    # Обновляем только переданные поля
    update_data = book_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)

    return book

# GET /books/ - Search book by title, author, or year
@app.get("/books/search/", response_model=List[schemas.BookResponse])
async def search_books(title: Optional[str] = None,
                       author: Optional[str] = None,
                       year: Optional[int] = None,
                       db: Session = Depends(get_db)):
    query = db.query(models.Book)
    # Добавляем фильтры, если параметры переданы
    if title:
        query = query.filter(models.Book.title.contains(title))
    if author:
        query = query.filter(models.Book.author.contains(author))
    if year:
        query = query.filter(year == models.Book.year)

    books = query.all()
    return books