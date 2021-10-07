#!/usr/bin/env python
import asyncio
import os
from asyncio import sleep

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine


# DATABASE SETTINGS
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    f"postgresql+asyncpg://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@{os.environ.get('POSTGRES_HOST')}:{os.environ.get('POSTGRES_PORT')}/{os.environ.get('POSTGRES_DB')}",
)
MAX_TRIES = 30


async def check_database_ready(database_url):
    """check to see if database is active"""

    print(f"connect:{database_url=}")
    engine = create_async_engine(database_url, future=True)

    connected = False
    tried = 0
    while not connected and tried < MAX_TRIES:
        tried += 1
        print(f"connect attempt {tried}/{MAX_TRIES}", end=":")
        try:
            async with engine.begin() as conn:
                await conn.execute(text("SELECT 1"))
                connected = True
                print("SUCCESS database ready")
        except (ConnectionRefusedError, ConnectionError):
            print("connection not ready")
            await sleep(2)
        finally:
            # clean up
            await engine.dispose()

    if tried >= MAX_TRIES:
        print("!!! DATABASE NOT ONLINE !!!")
        exit(1)


if __name__ == "__main__":
    asyncio.run(check_database_ready(DATABASE_URL))
