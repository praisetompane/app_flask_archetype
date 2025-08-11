import logging
import sys
from logging import log
from flask import Blueprint, Response, request, make_response
from src.app_flask_archetype.repository.common import computation_result_repository
from src.app_flask_archetype.api.validator import validate
from src.app_flask_archetype.core.computation import compute
from src.app_flask_archetype.gateway.external_api import retrieve_data
from logging import log
import asyncio

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


"""
    Guide:
        Place to implement your application's HTTP REST API endpoints.
"""

app_api = Blueprint("computation", __name__)


@app_api.route("/computation/", methods=["POST"])
def computation() -> Response:
    log(logging.INFO, "Handling a computation request")
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        request_data = request.json
        if not validate(request_data):
            return Response("Incorrectly formed request", 422)

        """
            Guide:
                Place to plug in delegation/s to your application's specific components to implement the endpoints goal/job/function.
        """
        data = asyncio.run(retrieve_data("MALARIA_CONF_CASES"))
        computation_result = compute(data)
        computation_result_repository.save(computation_result)

        log(logging.INFO, "Finished handling a computation request")
        return make_response({"computation_result": computation_result}, 201)
    else:
        log(logging.ERROR, f"Received unsupported content type. Terminating request")
        return Response("Content-Type not supported!")
