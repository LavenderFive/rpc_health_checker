import os
import requests
import time

from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

app = Flask(__name__)

SERVER_IP = os.getenv("SERVER_IP")
SERVER_PORT = os.getenv("SERVER_PORT")

# Time in seconds between current time and last block
ACCEPTABLE_DELTA = 60

@app.route("/health", methods=["GET"])
def health_check():
    # Get latest block data
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": ["latest", False],
        "id": 1
    }
    headers = {"Content-Type": "application/json"}
    url = f"http://{SERVER_IP}:{SERVER_PORT}"
    print(url)
    response = requests.post(url, headers=headers, json=payload)
    print(response.content)

    if response.status_code != 200:
        return "Error occurred while fetching latest block data", 500

    latest_block_data = response.json()
    current_time = int(time.time())

    # Check sync status
    if "result" not in latest_block_data:
        return "Sync status check failed", 500

    latest_block_time = int(latest_block_data["result"]["timestamp"], 16)
    block_time_delta = current_time - latest_block_time

    if latest_block_time is None or block_time_delta > ACCEPTABLE_DELTA:
        return "Block time delta exceeded acceptable limit", 500

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=53336)
