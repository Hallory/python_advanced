from operations import seed_data, read_data
from models import Base
from db import engine
Base.metadata.create_all(engine)

seed_data()
read_data()

