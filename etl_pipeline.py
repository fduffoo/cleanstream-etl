import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product

# Set up database connection
engine = create_engine('sqlite:///products.db')
Session = sessionmaker(bind=engine)
session = Session()

# Load CSV data
df = pd.read_csv('data/sample_data.csv')

# Clean Data
df.dropna(inplace=True)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Transform and Insert
for _, row in df.iterrows():
    product = Product(
        name=row['name'],
        category=row['category'],
        price=float(row['price']),
        quantity=int(row['quantity'])
    )
    session.add(product)

session.commit()
print(f"{len(df)} records inserted successfully.")
