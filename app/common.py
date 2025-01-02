import logging

logger = logging.getLogger(__name__)


def parse_request(req) -> tuple:
    # port = req.headers.get("Port")
    host = req.headers.get("Full-Upstream")
    ip_address = host.split(":")[0]
    port = host.split(":")[1]
    logger.info(f"{host} |Parsed IP address: {ip_address}, port: {port}")
    return ip_address, port
