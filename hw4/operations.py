from db import Session
from models import Category, Product
from sqlalchemy import func


def seed_data() -> None:
    session = Session()
    try:
        with session.begin():
            electronics = Category(
                name="Electronics",
                description="Gadgets and devices"
            )
            books = Category(
                name="Books",
                description="Printed and E-books"
            )
            clothes = Category(
                name="Clothes",
                description="Clothing for men and women"
            )

            products = [
                Product(name="Smartphone", price=299.99, in_stock=True, category=electronics),
                Product(name="Laptop", price=499.99, in_stock=True, category=electronics),
                Product(name="Sci-fi novel", price=15.99, in_stock=True, category=books),
                Product(name="Jeans", price=40.50, in_stock=True, category=clothes),
                Product(name="T-Shirt", price=20.00, in_stock=True, category=clothes),
            ]
            
            if session.query(Category).count() == 0:
                session.add_all([electronics, books, clothes, *products])
            
            


        print("Data seeded successfully!")

    finally:
        session.close()


def read_data() -> None:
    session = Session()
    try:
        with session.begin():
            categories = session.query(Category).all()
            for c in categories:
                print(c.name)
                for p in c.products:
                    print(p.name, p.price)
                        
    finally:
        session.close()
        
        
def get_first_smartphone_and_update_price() -> Product:
    session = Session()
    
    try:
        with session.begin():
            smartphone = session.query(Product).filter_by(name="Smartphone").first()
            if smartphone is None:
                print("Smartphone not found")
                return None
            smartphone.price = 349.99
    finally:
        session.close()
        

def aggregate_and_group_data_and_count_products()->None:
    session = Session()
    
    try:
        rows = (
            session.query(
                Category.name,
                func.count(Product.id).label("product_count")
            )
            .join(Product, Category.id == Product.category_id)
            .group_by(Category.name)
            .all()
        )
        
        for name, cnt in rows:
            print(f"{name}: {cnt} products")
            
    finally:
        session.close()
        

def categories_with_more_than_one_product()->None:
    session = Session()
    
    try:
        rows = (
            session.query(
                Category.name,
                func.count(Product.id).label("product_count")
            )
            .join(Product, Category.id == Product.category_id)
            .group_by(Category.name)
            .having(func.count(Product.id) > 1)
            .all()
            )
        
        for name, cnt in rows:
            print(f"{name}: {cnt} products")
            
    finally:
        session.close()