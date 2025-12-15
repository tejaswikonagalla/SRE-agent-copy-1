from uuid import UUID
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_database
from app.models import Book

from pydantic import BaseModel, Field

app = FastAPI()

class BookCreate(BaseModel):
    name: str
    author: str
    genre: str
    price: float

class BookUpdate(BaseModel):
    name: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    price: Optional[float] = None

class BookOut(BaseModel):
    id: UUID
    name: str
    author: str
    genre: str
    price: float

    class Config:
        orm_mode = True

@app.post("/books", response_model=BookOut)
def add_book(book: BookCreate, db: Session = Depends(get_database)):
    db_book = Book(
        name=book.name,
        author=book.author,
        genre=book.genre,
        price=book.price
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: UUID, book: BookUpdate, db: Session = Depends(get_database)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for field, value in book.dict(exclude_unset=True).items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: UUID, db: Session = Depends(get_database)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"detail": "Book deleted"}

@app.get("/books", response_model=List[BookOut])
def get_all_books(db: Session = Depends(get_database)):
    return db.query(Book).all()

@app.get("/books/genre/{genre}", response_model=List[BookOut])
def get_books_by_genre(genre: str, db: Session = Depends(get_database)):
    books = db.query(Book).filter(Book.genre == genre).all()
    return books

@app.get("/books/author/{author}", response_model=List[BookOut])
def get_books_by_author(author: str, db: Session = Depends(get_database)):
    books = db.query(Book).filter(Book.author == author).all()
    return books

@app.get("/books/{book_id}", response_model=BookOut)
def get_book_by_id(book_id: UUID, db: Session = Depends(get_database)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book