from typing import Dict

from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str
    year: int
    borrow: bool = Field(default=False)


class Library(BaseModel):
    books: Dict[str, Book] = Field(default_factory=dict)

