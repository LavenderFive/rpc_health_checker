# routes.py
from flask import Blueprint, request
from app.common import parse_request
from app.cosmos.cosmos import cosmos_health
from app.ethereum.ethereum import ethereum_health

api = Blueprint("api", __name__)


@api.route("/ethereum", methods=["GET"])
def ethereum_health_check():
    ip, port = parse_request(request)
    message, status = ethereum_health(ip, port)
    return message, status


@api.route("/cosmos", methods=["GET"])
def cosmos_health_check():
    ip, port = parse_request(request)
    message, status = cosmos_health(ip, port)
    return message, status
