from datetime import date, datetime
from pydantic import BaseModel


class NewsGetSchema(BaseModel):

    id: str
    title: str
    image_url: str
    parsed_date: datetime
    publication_date: date

    class Config:
        orm_mode = True


class NewsCreateSchema(BaseModel):

    title: str
    image_url: str
    publication_date: date


# P.S. не совсем DRY, но так вывод полей лучше
