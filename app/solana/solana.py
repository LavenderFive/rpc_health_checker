from datetime import datetime, timedelta, timezone
import requests


def solana_health(ip: str, port: str, acceptable_time_delta: int = 60):
    acceptable_time_delta = timedelta(seconds=acceptable_time_delta)

    # Get latest block data
    payload = {"jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": ["latest", False], "id": 1}
    headers = {"Content-Type": "application/json"}
    url = f"http://{ip}:{port}"
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return "Error occurred while fetching latest block data", 500

    latest_block_data = response.json()

    # Check sync status
    if "result" not in latest_block_data:
        return "Sync status check failed", 500

    current_dt = datetime.now(timezone.utc)
    latest_block_time = int(latest_block_data["result"]["timestamp"], 16)
    latest_dt = datetime.fromtimestamp(latest_block_time, timezone.utc)

    block_time_delta = current_dt - latest_dt

    if latest_dt is None or block_time_delta > acceptable_time_delta:
        return "Block time delta exceeded acceptable limit", 500
    return "OK", 200
