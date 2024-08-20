from pydantic import BaseModel

class Books(BaseModel):
    title: str
    author : str
    published_year : int
    isbn : str
    pages : int