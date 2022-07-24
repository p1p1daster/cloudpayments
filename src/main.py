from aiohttp import web
from aiohttp_basicauth import BasicAuthMiddleware

import src.conf as conf
from router import post_api_charge_rout
from src.middlewares import validation_middleware


def main() -> web.Application:
    auth = BasicAuthMiddleware(username=conf.USERNAME, password=conf.PASSWORD)

    app = web.Application(middlewares=[validation_middleware, auth])
    app.router.add_route(*post_api_charge_rout)

    return app


app = main()
