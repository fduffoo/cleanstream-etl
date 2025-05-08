import pandas as pd
import argparse
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product

# --- Set up argument parser ---
parser = argparse.ArgumentParser(description="ETL pipeline for CSV or JSON files.")
parser.add_argument('--file', required=True, help="Path to the input data file (.csv or .json)")
args = parser.parse_args()

input_file = args.file

# --- Check file type ---
file_ext = os.path.splitext(input_file)[-1].lower()

if file_ext == '.csv':
    df = pd.read_csv(input_file)
elif file_ext == '.json':
    df = pd.read_json(input_file)
else:
    raise ValueError("Unsupported file type. Please use a .csv or .json file.")

# --- Clean Data ---
df.dropna(inplace=True)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# --- Connect to DB ---
engine = create_engine('sqlite:///products.db')
Session = sessionmaker(bind=engine)
session = Session()

# --- Transform + Load ---
for _, row in df.iterrows():
    product = Product(
        name=row['name'],
        category=row['category'],
        price=float(row['price']),
        quantity=int(row['quantity'])
    )
    session.add(product)

session.commit()
print(f"{len(df)} records inserted successfully from {file_ext} file.")
