# Movie Analytics Pipeline

An end-to-end data pipeline project that fetches real-time movie data from the TMDb API, processes and stores it using PostgreSQL, and visualizes insights using Metabase. The pipeline is containerized with Docker and uses Amazon S3 for raw and cleaned data storage.

## 📊 Dashboard
Explore the interactive dashboard built with Metabase (local/private deployment):

> [🧪 Metabase Dashboard Screenshot] '_Movie Analytics Dashboard – Insights from TMDb API_.pdf'


## 🛠 Tech Stack

- **ETL & Processing**: Python, Pandas, TMDb API
- **Data Storage**: PostgreSQL (Dockerized)
- **Cloud Storage**: AWS S3 (raw + cleaned CSVs)
- **Visualization**: Metabase (Dockerized)
- **Containerization**: Docker, Docker Compose
- **Version Control**: Git + GitHub

---

## 📦 Features

- Extracts top movie data using TMDb API
- Maps genre IDs to names using genre lookup
- Cleans and transforms movie data
- Stores raw and cleaned data on S3
- Loads final data into PostgreSQL
- Visualizes 5 key insights using Metabase:
  - Monthly release trends
  - Most popular movies
  - Popular genres by average score
  - Genre distribution
  - Genre popularity by language

---

## 🚀 How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Movie_Analytics_Pipeline.git
cd Movie_Analytics_Pipeline

### 2. Set up environment variables
Create a .env file:

```bash
TMDB_API_KEY=your_tmdb_api_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
S3_BUCKET_NAME=your_bucket_name
PG_HOST=localhost
PG_PORT=5432
PG_DB=movies
PG_USER=your_user
PG_PASSWORD=your_password

### 3. Run Docker containers

```bash
docker-compose up --build

### 4. Run the ETL scripts

```bash
python fetch_movies.py
python genre_utils.py
python load_data.py
python s3_utils.py
python transform_genres.py


### 5. Visualize in Metabase

Access Metabase at http://localhost:3000, connect to PostgreSQL, and build your dashboard using SQL or the GUI.

### 6. Project Structure

```bash
Movie_Analytics_Pipeline/
├── fetch_movies.py
├── transform_genres.py
├── load_data.py
├── genre_utils.py
├── s3_utils.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── README.md


### 7. Acknowledgements

[TMDb API](https://www.themoviedb.org/) for providing movie data.
[Docker](https://www.docker.com/) for containerization.
[Metabase](https://www.metabase.com/) for easy visualization.


