# routes.py
from flask import Blueprint, request
from app.health_check_functions import switch

api = Blueprint("api", __name__)


@api.route("/health", methods=["GET"])
def health_check():
    host = request.headers.get("Full-Upstream")
    rpc_type = host[-2:]
    health_check_function = switch.get(rpc_type)

    if health_check_function:
        message, status = health_check_function(host)
    else:
        message, status = "Unknown RPC type", 400

    return message, status
