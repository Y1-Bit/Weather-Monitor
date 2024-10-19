from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


def create_engine(url: str, echo=False):
    """Create an asynchronous SQLAlchemy engine.

    Args:
        url (str): The database URL for the engine.
        echo (bool): If True, SQLAlchemy will log all the statements issued to the console.

    Returns:
        Engine: An instance of the asynchronous SQLAlchemy engine.
    """
    engine = create_async_engine(url, echo=echo)
    return engine


def create_session_pool(engine):
    """Create a session pool for interacting with the database.

    Args:
        engine: The SQLAlchemy engine to bind the session to.

    Returns:
        async_sessionmaker: A session factory for creating asynchronous sessions.
    """
    session_pool = async_sessionmaker(bind=engine, expire_on_commit=False)
    return session_pool
