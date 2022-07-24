from aiohttp import TCPConnector

import conf
from src.abstract_client import AbstractInteractionClient


class CloudPaymentsClient(AbstractInteractionClient):
    CONNECTOR = TCPConnector()
    REQUEST_TIMEOUT = conf.REQUEST_TIMEOUT
    CONNECT_TIMEOUT = conf.CONNECT_TIMEOUT
    SERVICE = conf.SERVICE
    BASE_URL = conf.BASE_URL


client = CloudPaymentsClient()
