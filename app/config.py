import os


LATITUDE = 55.7522  
LONGITUDE = 37.6156  

INTERVAL_MINUTES = 3


def get_db_url():
    """Constructs the database URL for connecting to the PostgreSQL database.

    Returns:
        str: Database URL for asyncpg connection.
    """
    POSTGRES_USER = os.getenv("POSTGRES_USER")  
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")  
    POSTGRES_DB = os.getenv("POSTGRES_DB")  
    DB_HOST = os.getenv("DB_HOST")  
    return f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}/{POSTGRES_DB}"
