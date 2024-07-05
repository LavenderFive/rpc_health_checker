# routes.py
from flask import Blueprint, request
from app.common import parse_request
from app.cosmos.cosmos import cosmos_health
from app.evm.ethereum import ethereum_health
from app.solana.solana import solana_health

api = Blueprint("api", __name__)

health_check_functions = {
    "45": ethereum_health,
    "57": cosmos_health,
    "17": cosmos_health,
    "90": cosmos_health,
    "99": solana_health,
}

@api.route("/health", methods=["GET"])
def health_check():
    ip, port = parse_request(request)
    rpc_type = port[:2]
    health_check_function = health_check_functions.get(rpc_type)

    if health_check_function:
        message, status = health_check_function(ip, port)
    else:
        message, status = "Unknown RPC type", 400

    return message, status
