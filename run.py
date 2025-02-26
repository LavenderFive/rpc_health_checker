import logging
import sys
import argparse
from flask import Flask
from app.routes import api  # Import the Blueprint

sys.stdout.reconfigure(line_buffering=True)

app = Flask(__name__)
app.register_blueprint(api)  # Register the Blueprint

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Run the Flask application.")
    parser.add_argument("--log-level", default="INFO", help="Set the logging level (default: INFO)")
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level.upper(), format="%(levelname)s | %(asctime)s | %(message)s")

    app.run(host="0.0.0.0", port=53336)

if __name__ == "__main__":
    main()
