from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product

# Set up database connection
engine = create_engine('sqlite:///products.db')
Session = sessionmaker(bind=engine)
session = Session()

# Option 1: View all products
def view_all():
    products = session.query(Product).all()
    for p in products:
        print(p)

# Option 2: Filter by category
def filter_by_category(category):
    results = session.query(Product).filter(Product.category == category).all()
    for p in results:
        print(p)

# Option 3: Filter by price range
def filter_by_price(min_price, max_price):
    results = session.query(Product).filter(Product.price >= min_price, Product.price <= max_price).all()
    for p in results:
        print(p)

# Option 4: Count total records
def count_products():
    count = session.query(Product).count()
    print(f"Total products: {count}")

# Run some queries
if __name__ == "__main__":
    print("📦 All Products:")
    view_all()

    print("\n🎯 Fitness Products:")
    filter_by_category("Fitness")

    print("\n💰 Products priced between $20 and $50:")
    filter_by_price(20, 50)

    print("\n🔢 Product Count:")
    count_products()
