import os

from dotenv import load_dotenv
from flask import Flask, request
from src.ethereum import ethereum_health

load_dotenv()

app = Flask(__name__)

SERVER_IP = os.getenv("SERVER_IP")
SERVER_PORT = os.getenv("SERVER_PORT")

# Time in seconds between current time and last block
ACCEPTABLE_DELTA = 60

@app.route("/ethereum", methods=["GET"])
def ethereum_health_check():
    ethereum_health(SERVER_IP, SERVER_PORT, ACCEPTABLE_DELTA)

@app.route("/cosmos", methods=["GET"])
def health_check():
    print(f"Request Method: {request.method}")
    print(f"Request URL: {request.url}")
    print(f"Request Headers: {request.headers}")
    # Add your response logic here, for example:
    return "Health Check OK", 200

def main():
    app.run(host="0.0.0.0", port=53336)

main()
