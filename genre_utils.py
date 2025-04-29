
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")  # Get API key for TMDb

def get_genre_mapping():
    """
    Fetch genre ID-to-name mapping from TMDb API.

    Returns:
        Dictionary with genre IDs as keys and genre names as values.
    """
    url = f"https://api.themoviedb.org/3/genre/movie/list"

    # Make an API request to get genres
    response = requests.get(url, params={"api_key": api_key, "language": "en-US"})

    # Extract genres and create a mapping dictionary
    genres = response.json()["genres"]
    return {genre["id"]: genre["name"] for genre in genres}
