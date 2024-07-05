import requests
import time

def ethereum_health(ip: str, port: str, acceptable_time_delta: int = 60):
    # Get latest block data
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": ["latest", False],
        "id": 1
    }
    headers = {"Content-Type": "application/json"}
    url = f"http://{ip}:{port}"
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

    if latest_block_time is None or block_time_delta > acceptable_time_delta:
        return "Block time delta exceeded acceptable limit", 500

    return "OK", 200
