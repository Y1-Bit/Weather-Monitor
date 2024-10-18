from datetime import datetime
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.functions import func


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""
    pass


class TimestampMixin:
    """Mixin class that adds timestamp fields for tracking record creation time."""
    
    # Column to store the creation timestamp of the record, with a default value of the current time
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
