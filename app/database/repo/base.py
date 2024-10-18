from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepo:
    """Base repository class for handling database operations."""
    
    def __init__(self, session: AsyncSession):
        """
        Initialize the repository with a database session.

        Args:
            session (AsyncSession): An asynchronous session for interacting with the database.
        """
        self.session: AsyncSession = session  # Store the provided session for later use
