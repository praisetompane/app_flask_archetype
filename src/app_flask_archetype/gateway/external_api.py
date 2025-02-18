import requests

from logging import log
import logging

"""
    Guide:
        Place to implement your application's external API data requests.
"""


def retrieve_data(indicator_code):
    try:
        url = f"https://ghoapi.azureedge.net/api/{indicator_code}"
        log(logging.INFO, f"Contacting API: {url} ")
        request = requests.get(url)
        return request.json()["value"]
    except Exception as e:
        log(logging.ERROR,
            f"Encountered an error while invoking endpoint. ERROR = {e}")
        raise


def send_data(data):
    try:
        url = f"https://some_api"
        log(logging.INFO, f"Contacting {url} ")
        return requests.post(url)
    except Exception as e:
        log(logging.ERROR,
            f"Encountered an error while invoking endpoint. ERROR = {e}")
        raise
