from models import Category, Product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///hw3.db')

Session = sessionmaker(bind=engine)


electronics = Category(name="Electronics", description="Gadgets and devices")
books = Category(name="Books", description="Printed and E-books")
clothes = Category(name="Clothes", description="Clothing for men and women")

smartphone = Product(name="Smartphone", price=299.99, in_stock=True, category=electronics)
laptop = Product(name="Laptop", price=499.99, in_stock=True, category=electronics)
sci_fi = Product(name="Sci-fi", price=15.99, in_stock=True, category=books)
jeans = Product(name="Jeans", price=40.50, in_stock=True, category=clothes)
tshirt = Product(name="T-Shirt", price=20.00, in_stock=True, category=clothes)

def add_categories():
    session = Session()
    with session.begin():
        session.add(electronics)
        session.add(books)
        session.add(clothes)
    session.close()
def add_products():
    session = Session()
    with session.begin():
        session.add(smartphone)
        session.add(laptop)
        session.add(sci_fi)
        session.add(jeans)
        session.add(tshirt)
    session.close()
