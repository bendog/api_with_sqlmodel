import os

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    f'postgresql+asyncpg://{os.environ.get("PGUSER")}:{os.environ.get("PGPASSWORD")}@{os.environ.get("PGHOST")}:{os.environ.get("PGPORT", 5432)}/{os.environ.get("PGDATABASE")}',
)
