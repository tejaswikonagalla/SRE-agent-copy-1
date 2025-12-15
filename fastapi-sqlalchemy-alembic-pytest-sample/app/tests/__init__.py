# Import necessary modules to ensure the tests package is recognized and any required modules are available.
import os
import sys

# Add the app directory to the sys.path to ensure modules can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'app')))

# Import test modules if they exist
try:
    import test_module1
    import test_module2
except ImportError:
    # If specific test modules are not found, pass silently
    pass

# Ensure alembic migrations are applied before running tests
from alembic import command
from alembic.config import Config

def run_migrations():
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), '..', '..', 'alembic.ini'))
    try:
        command.upgrade(alembic_cfg, 'head')
    except Exception as e:
        print(f"Migration failed: {e}")
        raise

# Run migrations when the module is imported, not just when executed as a script
run_migrations()