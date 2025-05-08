from sqlalchemy import create_engine
from models import Base

# Create SQLite DB
engine = create_engine('sqlite:///products.db')
Base.metadata.create_all(engine)

print("Database and tables created.")
