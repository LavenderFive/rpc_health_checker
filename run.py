import logging
import sys
from flask import Flask
from app.routes import api  # Import the Blueprint

sys.stdout.reconfigure(line_buffering=True)

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(asctime)s | %(message)s")

app = Flask(__name__)
app.register_blueprint(api)  # Register the Blueprint

logger = logging.getLogger(__name__)


def main():
    app.run(host="0.0.0.0", port=53336)


main()
