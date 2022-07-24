from aiohttp.web_response import json_response

from abstract_client import InteractionResponseError
from schemas import charge_schema
from src.client import client
from src.router import endpoint_url


async def charge_payment_handler(req):
    req_data = await req.json()
    schema = charge_schema()
    schema.validate(req_data)

    url = client.endpoint_url(endpoint_url)

    try:
        headers = {"Authorization": req.headers.get("Authorization", "")}
        response_data = await client.post(
            interaction_method="charge",
            url=url,
            headers=headers,
            json=req_data,
        )
    except InteractionResponseError as exc:
        return json_response(
            dict(success=False, error=dict(message=exc.message)), status=418  # :))
        )
    return json_response(response_data)
