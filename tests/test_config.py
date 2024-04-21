"""Provides test cases for app/config.py."""

import os


vars: dict = {
    "APP_VERSION": "dev",
    "WEBEX_API_KEY": "testing",
    "SENTRY_ENABLED": "false",
    "SENTRY_DSN": "http://localhost"
}


for var, value in vars.items():
    os.environ[var] = value

# needs to be imported AFTER environment variables are set
from app.config import config  # pragma: no cover


def test_config() -> None:
    assert config.webex_token == vars["WEBEX_API_KEY"]
    assert config.version == vars["APP_VERSION"]
    assert config.sentry_enabled == bool(vars["SENTRY_ENABLED"].lower() == "true")
