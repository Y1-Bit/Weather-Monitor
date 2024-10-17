from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


def create_engine(url: str, echo=False):
    engine = create_async_engine(url, echo=echo)
    return engine


def create_session_pool(engine):
    session_pool = async_sessionmaker(bind=engine, expire_on_commit=False)
    return session_pool
