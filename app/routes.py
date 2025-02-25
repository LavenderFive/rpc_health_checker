# routes.py
import logging
from flask import Blueprint, request
from app.health_check_functions import switch

api = Blueprint("api", __name__)
logger = logging.getLogger(__name__)


@api.route("/health", methods=["GET"])
def health_check():
    host = request.headers.get("Full-Upstream")
    rpc_type = host[-2:]
    health_check_function = switch.get(rpc_type)

    logger.debug(f"{host} | {health_check_function}")

    try:
        if health_check_function:
            message, status = health_check_function(host)
        else:
            message, status = "Unknown RPC type", 400
    except Exception as e:
        logger.error(f"{host} | {e}")
        message, status = "Error occurred while fetching health data", 500

    logger.debug(f"{host} | {message} | {status}")
    return message, status


@api.route("/healthz", methods=["GET"])
def healthz_check():
    return "OK", 200
