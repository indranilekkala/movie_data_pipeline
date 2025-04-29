
import ast  # To safely convert string lists to Python lists
import dbm  
import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch PostgreSQL credentials from environment variables
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB = os.getenv("PG_DB")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")

# Create SQLAlchemy engine for PostgreSQL connection
engine = create_engine(f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}")

# Create 'movies' table in PostgreSQL if it doesn't already exist
with engine.connect() as connection:
    connection.execute(text("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title VARCHAR,
        genre_ids INTEGER[],
        genre_names TEXT[],
        release_date DATE,
        popularity FLOAT,
        vote_average FLOAT,
        original_language VARCHAR(8)
    );
"""))

# Load cleaned movie data from CSV file
movies_df = pd.read_csv("popular_movies_cleaned.csv")

# Convert string-formatted lists into real Python lists
movies_df['genre_ids'] = movies_df['genre_ids'].apply(ast.literal_eval)
movies_df['genre_names'] = movies_df['genre_names'].apply(ast.literal_eval)

# Upload the DataFrame into PostgreSQL table (replace if it already exists)
movies_df.to_sql("movies", engine, if_exists="replace", index=False, method="multi")

# Confirmation message
print("✅ Movies loaded into PostgreSQL from CSV!")
