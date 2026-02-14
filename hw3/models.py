from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(100), nullable=False)
    price: float = Column(Numeric, nullable=False)
    in_stock = Column(Boolean, nullable=False)
     
    category_id: int = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="products")
     
class Category(Base):
    __tablename__ = 'categories'
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(100), nullable=False)
    description: str = Column(String(255), nullable=False)
    
    products = relationship("Product", back_populates="category")
    