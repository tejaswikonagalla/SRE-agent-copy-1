# Marks the app directory as a Python package.

# Import necessary modules to ensure they are recognized as part of the package
from .main import app

# Ensure all submodules are imported to avoid ModuleNotFoundError
import os
import sys

# Add the app directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import other necessary modules or packages within the app
from . import models
from . import database
from . import routes

# Initialize the database and apply migrations
from .database import engine
from .models import Base

# Import alembic to handle migrations
from alembic.config import Config
from alembic import command

# Create all tables in the database if they do not exist
Base.metadata.create_all(bind=engine)

# Apply migrations using Alembic
alembic_cfg = Config(os.path.join(os.path.dirname(__file__), 'alembic.ini'))

# Ensure the alembic.ini file exists and is correctly configured
if os.path.exists(alembic_cfg.config_file_name):
    command.upgrade(alembic_cfg, 'head')
else:
    raise FileNotFoundError("alembic.ini file not found. Ensure it exists in the app directory.")