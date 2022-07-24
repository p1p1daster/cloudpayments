from aiohttp.web import json_response
from aiohttp.web_middlewares import middleware
from marshmallow.exceptions import ValidationError


@middleware
async def validation_middleware(request, handler):
    try:
        return await handler(request)
    except ValidationError as exc:
        return json_response(dict(error=exc.messages, success=False), status=418)  # :))
