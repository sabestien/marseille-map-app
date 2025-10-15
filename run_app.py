import os
import sys
from streamlit.web import cli as stcli

# This is essential to make sure the app can find the Excel file
# and the .streamlit folder when running from the bundled .exe
def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    # Set the path to your main Streamlit app script
    app_path = get_resource_path('app.py')

    # Set the path to your config file
    config_path = get_resource_path('.streamlit/config.toml')

    # Arguments for the streamlit run command
    # --server.headless is important for packaged apps
    args = [
        "run",
        app_path,
        "--server.headless", "true",
        "--server.enableCORS", "false",
        "--server.port", "8501" # You can choose a different port
    ]

    # Insert the config file path into the arguments list
    sys.argv = args
    
    # Run streamlit
    stcli.main()