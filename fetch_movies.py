
import requests
import os
import pandas as pd
from dotenv import load_dotenv
from s3_utils import upload_to_s3  # Custom function to upload files to S3

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")  # Get API key for TMDb

# Output path to save the movie data locally
output_path = "/mydata/popular_movies.csv"

# Set base URLs for TMDb API
base_url = "https://api.themoviedb.org/3"
movie_url = f"{base_url}/movie/popular"

def fetch_movies(pages=1):
    """
    Fetch popular movies from TMDb API.

    Args:
        pages (int): Number of pages to fetch (each page ~20 movies)

    Returns:
        List of dictionaries with movie details
    """
    movies = []
    for page in range(1, pages + 1):
        # Make an API request for each page
        response = requests.get(
            movie_url,
            params={
                "api_key": api_key,
                "language": "en-US",
                "page": page
            }
        )
        data = response.json()

        # Extract relevant fields from each movie
        for movie in data.get("results", []):
            movies.append({
                "id": movie.get("id"),
                "title": movie.get("title"),
                "genre_ids": movie.get("genre_ids"),
                "vote_average": movie.get("vote_average"),
                "release_date": movie.get("release_date"),
                "original_language": movie.get("original_language"),
                "popularity": movie.get("popularity")
            })
    return movies

if __name__ == "__main__":
    # Fetch popular movies (2 pages = around 40 movies)
    movies = fetch_movies(pages=2)
    
    # Create a DataFrame from the movie list
    df = pd.DataFrame(movies)
    
    # Save the data locally as CSV
    print("Saved to popular_movies.csv")
    with open(output_path, "w") as f:
        df.to_csv(f, index=False)

    # Upload the CSV to S3 bucket in 'raw' folder
    upload_to_s3("popular_movies.csv", os.getenv("S3_BUCKET_NAME"), "raw/popular_movies.csv")
