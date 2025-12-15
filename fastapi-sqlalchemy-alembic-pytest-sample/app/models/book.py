from sqlalchemy import Column, String, Float
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.models.model_base import ModelBase

class Book(ModelBase):
    __tablename__ = "books"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=True)
    price = Column(Float, nullable=False)