# Import necessary modules to ensure the tests package is recognized and any required modules are available.
import os
import sys

# Add the app directory to the sys.path to ensure modules can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Import test modules if they exist
try:
    from . import test_module1
    from . import test_module2
except ImportError:
    # If specific test modules are not found, pass silently
    pass