#!/usr/local/bin/python3

import sentry_sdk
from sentry_sdk.integrations.stdlib import StdlibIntegration
from webex_bot.webex_bot import WebexBot

from app import close, meme
from app.config import config

if config.sentry_enabled:
    apm = sentry_sdk.init(
        dsn=config.sentry_dsn,
        enable_tracing=True,
        environment=config.environment,
        release=config.version,
        integrations=[StdlibIntegration()],
        spotlight=True,
    )


def create_bot() -> WebexBot:
    """Create a Bot object."""
    bot = WebexBot(
        teams_bot_token=config.webex_token,
        approved_domains=["cisco.com"],
        bot_name="MemeBot",
        include_demo_commands=False,
    )
    return bot


def main() -> None:
    bot: WebexBot = create_bot()
    bot.add_command(meme.MakeMemeCommand())
    bot.add_command(close.ExitCommand())
    bot.commands.remove(bot.help_command)
    bot.help_command = meme.MakeMemeCommand()
    bot.run()


if __name__ == "__main__":
    main()
