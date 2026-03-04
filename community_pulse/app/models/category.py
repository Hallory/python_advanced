from sqlalchemy import  Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Category(Base):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    questions: Mapped[list["Question"]] = relationship("Question", back_populates="category")
    
    