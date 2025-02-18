from flask import Blueprint, Response

"""
    Guide:
        Place to implement your application's HTTP health check REST API endpoints.
"""

health_check_api = Blueprint("health_check_api", __name__)


@health_check_api.route("/ping/")
def ping() -> Response:
    return Response("pong", 200)
