from logging import log
import logging
import aiohttp
"""
    Guide:
        Place to implement your application's external API data requests.
"""


async def execute_request(session, url):
    async with session.get(url) as resp:
        return await resp.json()

async def retrieve_data(indicator_code):
    async with aiohttp.ClientSession() as session:
        try:
            url = f"https://ghoapi.azureedge.net/api/{indicator_code}"
            log(logging.INFO, f"Contacting API: {url} ")
            result = await execute_request(session, url)
            return result["value"]
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
