from pydantic import BaseModel
from typing import Optional


# Схема для создания книги
class BookCreate(BaseModel):
    title: str
    author: str
    year: int | None = None


# Схема для обновления книги
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None


# Схема для отображения книги
class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None

    class Config:
        orm_mode = True  # Для работы с ORM объектами