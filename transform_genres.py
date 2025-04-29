
import os
import pandas as pd
from genre_utils import get_genre_mapping  # Custom function to get genre name mapping from TMDb API
import ast  # Used to safely convert stringified lists into Python lists
from s3_utils import upload_to_s3  # Custom function to upload files to AWS S3

# Load the raw movie data from CSV
df = pd.read_csv("popular_movies.csv")

# Get the mapping of genre IDs to genre names using the TMDb API
genre_map = get_genre_mapping()

# Function to convert genre ID list into genre name list
def map_genres(id_list):
    # If the genre IDs are stored as strings, convert them to actual lists
    if isinstance(id_list, str):
        id_list = ast.literal_eval(id_list)
    # Map each ID to its corresponding name using genre_map
    return [genre_map.get(genre_id, "Unknown") for genre_id in id_list]

# Create a new column with readable genre names
df["genre_names"] = df["genre_ids"].apply(map_genres)

# Save the cleaned data (with genre names) to a CSV file
output_path = "/mydata/popular_movies.csv"
with open(output_path, "w") as f:
    df.to_csv(f, index=False)

print("Saved cleaned data with genre names.")

# Upload the cleaned CSV file to S3 in the 'cleaned' folder
upload_to_s3("popular_movies_cleaned.csv", os.getenv("S3_BUCKET_NAME"), "cleaned/popular_movies_cleaned.csv")
