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