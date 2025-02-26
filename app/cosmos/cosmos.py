import requests
import logging

from datetime import datetime, timedelta, timezone

logger = logging.getLogger(__name__)


def modify_host(host_rpc):
    host, port = host_rpc.split(":")
    new_port = port[:-2] + "57"
    return f"{host}:{new_port}"


def cosmos_health(host: str, acceptable_time_delta: int = 20) -> tuple:
    acceptable_time_delta = timedelta(seconds=acceptable_time_delta)

    # rpc is used because /node_info endpoint isn't always available. In addition,
    # after extensive tests, /status and /node_info are roughly the same speed.
    if not host.endswith("57"):
        host = modify_host(host)

    url = f"http://{host}/status"
    try:
        response = requests.post(url)
    except ConnectionError as e:
        logger.error(f"{host} | {e}")
        return "Node is down", 502

    if response.status_code != 200:
        return "Error occurred while fetching latest block data", 502

    latest_block_data = response.json()

    logger.debug(f"{host} | {latest_block_data}")

    # Check sync status
    if "result" in latest_block_data:
        latest_block_data = latest_block_data["result"]

    current_dt = datetime.now(timezone.utc)
    tx_index = latest_block_data["node_info"]["other"]["tx_index"]
    if tx_index == "off":
        logger.error(f"{host} | Tx index is off")
        return "Tx index is off", 500
    latest_block_time = latest_block_data["sync_info"]["latest_block_time"]
    truncated_time_str = latest_block_time[:-4] + "Z"
    latest_block_dt = datetime.strptime(truncated_time_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
    block_time_delta = current_dt - latest_block_dt

    if latest_block_time is None or block_time_delta > acceptable_time_delta:
        return "Block time delta exceeded acceptable limit", 500
    return "OK", 200
