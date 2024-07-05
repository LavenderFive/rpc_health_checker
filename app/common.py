def parse_request(req) -> tuple:
    port = req.headers.get("Port")
    host = req.headers.get("Host")
    ip_address = host.split(":")[0]
    return ip_address, port
