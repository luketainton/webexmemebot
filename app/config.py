"""Configuration module."""

import os


class Config:
    """Configuration module."""
    def __init__(self) -> None:
        """Configuration module."""
        self.__environment: str = os.environ.get("APP_LIFECYCLE", "DEV").upper()
        self.__version: str = os.environ["APP_VERSION"]
        self.__webex_token: str = os.environ["WEBEX_API_KEY"]
        self.__sentry_dsn: str = os.environ.get("SENTRY_DSN", "")
        self.__sentry_enabled: bool = bool(
            os.environ.get("SENTRY_ENABLED", "False").upper() == "TRUE"
            and self.__sentry_dsn != ""
        )

    @property
    def environment(self) -> str:
        """Returns the current app lifecycle."""
        return self.__environment

    @property
    def version(self) -> str:
        """Returns the current app version."""
        return self.__version

    @property
    def sentry_enabled(self) -> bool:
        """Returns True if Sentry SDK is enabled, else False."""
        return self.__sentry_enabled

    @property
    def sentry_dsn(self) -> str:
        """Returns the Sentry DSN value if Sentry SDK is enabled AND
        Sentry DSN is set, else blank string."""
        if not self.__sentry_enabled:
            return ""
        return self.__sentry_dsn

    @property
    def webex_token(self) -> str:
        """Returns the Webex API key."""
        return self.__webex_token


config: Config = Config()
