
import os
import ast
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB = os.getenv("PG_DB")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")

# Create SQLAlchemy engine
engine = create_engine(f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}")


# Helper function to run query and plot
def run_query_and_plot(query, x_col, y_col, title, color='skyblue'):
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
    df.plot(kind='bar', x=x_col, y=y_col, legend=False, color=color)
    plt.title(title)
    plt.xlabel(x_col.capitalize())
    plt.ylabel(y_col.capitalize())
    plt.tight_layout()
    plt.show()

# Query 1: Top 10 Genres by Movie Count
query1 = """
SELECT unnest(genre_names::TEXT[]) AS genre, COUNT(*) AS count
FROM movies
GROUP BY genre
ORDER BY count DESC
LIMIT 10;
"""
run_query_and_plot(query1, 'genre', 'count', 'Top 10 Movie Genres')

# Query 2: Top 10 Genres by Average Rating
query2 = """
SELECT unnest(genre_names::TEXT[]) AS genre, AVG(vote_average) AS avg_rating
FROM movies
GROUP BY genre
ORDER BY avg_rating DESC
LIMIT 10;
"""
run_query_and_plot(query2, 'genre', 'avg_rating', 'Top 10 Genres by Avg Rating', color='orange')

# Query 3: Most Popular Movies (by popularity)
query3 = """
SELECT title, popularity
FROM movies
ORDER BY popularity DESC
LIMIT 10;
"""
run_query_and_plot(query3, 'title', 'popularity', 'Top 10 Most Popular Movies', color='green')

# Query 4: Release Year Distribution (optional if you have release_date column parsed)
query4 = """
SELECT EXTRACT(YEAR FROM release_date::date) AS year, COUNT(*) AS count
FROM movies
GROUP BY year
ORDER BY year;
"""
with engine.connect() as conn:
        df = pd.read_sql(text(query4), conn)
df.plot(kind='line', x='year', y='count', marker='o')
plt.title('Number of Movies Released Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.grid(True)
plt.tight_layout()
plt.show()

# Query 5: Most Popular Genre Per Language
query5 = """
SELECT popular_genre.genre, popular_genre.original_language, popular_genre.avg_popularity
FROM (
    SELECT 
        unnest(genre_names::TEXT[]) AS genre,
        original_language,
        AVG(popularity) AS avg_popularity,
        RANK() OVER (PARTITION BY original_language ORDER BY AVG(popularity) DESC) AS rank
    FROM movies
    GROUP BY original_language, genre
) as popular_genre
WHERE popular_genre.rank = 1
ORDER BY avg_popularity DESC;
"""
with engine.connect() as conn:
        df = pd.read_sql(text(query5), conn)
df.plot(kind='barh', x='genre', y='avg_popularity', color='purple')
plt.title('Most Popular Genre Per Language')
plt.xlabel('Average Popularity')
plt.ylabel('Genre')
plt.tight_layout()
plt.show()





