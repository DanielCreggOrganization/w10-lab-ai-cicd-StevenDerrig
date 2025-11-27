# Entry point for the application.
from . import app    # For application discovery by the 'flask' command. 
from . import views  # For import side-effects of setting up routes. 

# In hello_app/webapp.py
AWS_SECRET_KEY = "AKIA1234567890"

# Time-saver: output a URL to the VS Code terminal so you can easily Ctrl+click to open a browser
# print('http://127.0.0.1:5000/hello/VSCode')

def process_request():
    """
    Process an incoming request.

    Returns:
        bool: True if the processing was successful.
    """
    return True
