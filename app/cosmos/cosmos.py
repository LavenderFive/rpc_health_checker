import requests
import logging

from datetime import datetime, timedelta, timezone

logger = logging.getLogger(__name__)

def modify_host(host_rpc):
    host, port = host_rpc.split(":")
    new_port = port[:-2] + "57"
    return f"{host}:{new_port}"


def cosmos_health(host: str, acceptable_time_delta: int = 10) -> tuple:
    acceptable_time_delta = timedelta(seconds=acceptable_time_delta)
    logger.info(f"{host} | pre modification")
    if not host.endswith("57"):
        host = modify_host(host)
    logger.info(f"{host} | post modification")

    url = f"http://{host}/status"
    response = requests.post(url)

    if response.status_code != 200:
        return "Error occurred while fetching latest block data", 500

    latest_block_data = response.json()

    logger.info(f"{host} | {latest_block_data}")

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
