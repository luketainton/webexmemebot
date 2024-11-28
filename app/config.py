"""Configuration module."""

import os


class Config:
    """Configuration module."""

    def __init__(self) -> None:
        """Configuration module."""
        self.__environment: str = os.environ.get("APP_LIFECYCLE", "DEV").upper()
        self.__version: str = os.environ["APP_VERSION"]
        self.__webex_token: str = os.environ["WEBEX_API_KEY"]

    @property
    def environment(self) -> str:
        """Returns the current app lifecycle."""
        return self.__environment

    @property
    def version(self) -> str:
        """Returns the current app version."""
        return self.__version

    @property
    def webex_token(self) -> str:
        """Returns the Webex API key."""
        return self.__webex_token


config: Config = Config()
