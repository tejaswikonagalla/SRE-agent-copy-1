from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

# Use a naming convention to avoid migration issues
convention = {
    "ix": 'ix_%(table_name)s_%(column_0_name)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    author = Column(String, index=True)

    def __init__(self, title, author):
        self.title = title
        self.author = author