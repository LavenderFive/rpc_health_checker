def parse_request(req) -> tuple:
    # port = req.headers.get("Port")
    host = req.headers.get("Full-Upstream")
    ip_address = host.split(":")[0]
    port = host.split(":")[1]
    return ip_address, port
