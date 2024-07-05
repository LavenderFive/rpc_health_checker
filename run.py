from dotenv import load_dotenv
from flask import Flask, request
from app.ethereum import ethereum_health
from app.cosmos import cosmos_health

load_dotenv()

app = Flask(__name__)

# Time in seconds between current time and last block
ACCEPTABLE_DELTA = 60


@app.route("/ethereum", methods=["GET"])
def ethereum_health_check():
    ip, port = parse_request(request)
    message, status = ethereum_health(ip, port)
    return message, status


@app.route("/cosmos", methods=["GET"])
def health_check():
    ip, port = parse_request(request)
    message, status = cosmos_health(ip, port)
    return message, status


def parse_request(req) -> tuple:
    port = req.headers.get("Port")
    host = req.headers.get("Host")
    ip_address = host.split(":")[0]
    return ip_address, port


def main():
    app.run(host="0.0.0.0", port=53336)


main()
