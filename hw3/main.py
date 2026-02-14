from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Category, Product
engine = create_engine('sqlite:///hw3.db')

Session = sessionmaker(bind=engine)
session = Session()


def get_categories():
    categories = session.query(Category).all()
    return categories


def get_products():
    products = session.query(Product).all()
    return products




