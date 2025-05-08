# 🧼 CleanStream ETL

A simple yet powerful Python ETL pipeline that ingests raw data from a CSV or JSON file, cleans and transforms it using Pandas, and loads it into a SQLite database using SQLAlchemy.

---

## 🚀 Features

- ✅ Extracts data from CSV & JSON
- 🧹 Cleans and normalizes column names
- 🔁 Transforms raw records into Python ORM objects
- 💾 Loads clean data into a SQLite database
- 🔎 Includes a query script to filter, search, and count records
- ⚙️ Accepts dynamic input file path via command-line argument

---

## 🧰 Tech Stack

- **Python**
- **Pandas**
- **SQLAlchemy**
- **SQLite**
- (Optional: PostgreSQL for scalability)

---

## 🗂️ Project Structure

```
CleanStream-ETL/
├── data/
│   ├── sample_data.csv
│   └── sample_data.json
├── models.py          # SQLAlchemy table schema
├── db_setup.py        # Initializes database
├── etl_pipeline.py    # Extracts, cleans, loads data
├── query.py           # Reads and filters from DB
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/fduffoo/cleanstream-etl.git
   cd cleanstream-etl
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python db_setup.py
   ```

5. **Run the ETL pipeline**
   ```bash
   python etl_pipeline.py --file data/sample_data.csv
   # or for JSON:
   python etl_pipeline.py --file data/sample_data.json
   ```

6. **Query the data**
   ```bash
   python query.py
   ```

---

## 🧠 What You’ll Learn

- How to build a basic ETL pipeline using Python
- How to use Pandas for data cleaning
- How to model and interact with a database using SQLAlchemy ORM
- How to organize a Python project professionally
- How to make your Python scripts dynamic and user-friendly with argparse

---

## 🔮 Future Enhancements

- PostgreSQL version with cloud deployment
- Logging and error handling
- Docker support for deployment
- CLI menu interface for queries

---

## 📸 Demo (Coming Soon)

Screenshots or terminal output examples

---

## 📬 Contact

Built by [Fernando Duffoo](https://github.com/fduffoo) – feel free to reach out or fork the project!
