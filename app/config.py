import os

# Load environment variables for PostgreSQL database connection
POSTGRES_USER = os.getenv("POSTGRES_USER")  # Database username
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")  # Database password
POSTGRES_DB = os.getenv("POSTGRES_DB")  # Database name
DB_HOST = os.getenv("DB_HOST")  # Database host address

# Default geographic coordinates for fetching weather data (latitude and longitude)
LATITUDE = 55.7522  # Latitude for Moscow
LONGITUDE = 37.6156  # Longitude for Moscow

# Time interval (in minutes) for scheduling weather data fetching
INTERVAL_MINUTES = 3


def get_db_url():
    """Constructs the database URL for connecting to the PostgreSQL database.

    Returns:
        str: Database URL for asyncpg connection.
    """
    return f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}/{POSTGRES_DB}"
