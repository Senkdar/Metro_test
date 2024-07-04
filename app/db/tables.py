from datetime import datetime

from sqlalchemy import Column, String, Date, DateTime
from uuid import uuid4

from app.db.settings import Base


class News(Base):

    __tablename__ = "news"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    title = Column(String, index=True)
    image_url = Column(String)
    publication_date = Column(Date)
    parsed_date = Column(DateTime, default=datetime.utcnow)
