import requests
from datetime import datetime, timedelta, timezone


def cosmos_health(ip: str, port: str, acceptable_time_delta: int = 60) -> tuple:
    acceptable_time_delta = timedelta(seconds=acceptable_time_delta)

    url = f"http://{ip}:{port}/status"
    response = requests.post(url)

    if response.status_code != 200:
        return "Error occurred while fetching latest block data", 500

    latest_block_data = response.json()

    # Check sync status
    if "result" not in latest_block_data:
        return "Sync status check failed", 500

    current_dt = datetime.now(timezone.utc)
    latest_block_time = latest_block_data["result"]["sync_info"]["latest_block_time"]
    truncated_time_str = latest_block_time[:-4] + "Z"
    latest_block_dt = datetime.strptime(truncated_time_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
    block_time_delta = current_dt - latest_block_dt

    if latest_block_time is None or block_time_delta > acceptable_time_delta:
        return "Block time delta exceeded acceptable limit", 500
    return "OK", 200
