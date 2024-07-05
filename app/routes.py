# routes.py
from flask import Blueprint, request
from app.common import parse_request
from app.health_check_functions import switch

api = Blueprint("api", __name__)

@api.route("/health", methods=["GET"])
def health_check():
    ip, port = parse_request(request)
    rpc_type = port[-2:]
    health_check_function = switch.get(rpc_type)

    if health_check_function:
        message, status = health_check_function(ip, port)
    else:
        message, status = "Unknown RPC type", 400

    return message, status
