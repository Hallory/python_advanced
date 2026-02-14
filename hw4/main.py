from operations import add_categories, add_products
from models import Base
from operations import engine
Base.metadata.create_all(engine)

add_categories()
add_products()


