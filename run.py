from main import app

from config.config import CONFIG_APP
from waitress import serve

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=CONFIG_APP["app"]["port"], url_scheme='https')