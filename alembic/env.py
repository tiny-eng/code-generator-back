from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
import os

# Add app folder to Python path so we can import models
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

# Import your database and models
from app.database import DATABASE_URL, Base
from app.models import user_model  # 👈 import your user model

# Alembic Config object
config = context.config

# Use the database URL from your FastAPI app
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Setup logging from config file
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Pass the metadata to Alembic so it can autogenerate migrations
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
