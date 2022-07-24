import os

from environ import Env

env = Env()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env.read_env(os.path.join(BASE_DIR, ".env"))
# ------------------------------------------------------

REQUEST_TIMEOUT = env.int("REQUEST_TIMEOUT", default=30)
CONNECT_TIMEOUT = env.int("CONNECT_TIMEOUT", default=5)
SERVICE = env.str("SERVICE")
BASE_URL = env.email_url("BASE_URL")
# ------------------------------------------------------

USERNAME = env.str("USERNAME")
PASSWORD = env.str("PASSWORD")
