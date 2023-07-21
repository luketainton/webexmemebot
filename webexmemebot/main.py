#!/usr/local/bin/python3

import os

from webex_bot.webex_bot import WebexBot

from webexmemebot import exit, meme


WBX_API_KEY: str = os.environ["WEBEX_API_KEY"]


def create_bot() -> WebexBot:
    """Create a Bot object."""
    bot = WebexBot(
        teams_bot_token=WBX_API_KEY,
        approved_domains=["cisco.com"],
        bot_name="MemeBot",
        include_demo_commands=False,
    )
    return bot


def main():
    bot: WebexBot = create_bot()
    bot.add_command(meme.MakeMemeCommand())
    bot.add_command(exit.ExitCommand())
    bot.commands.remove(bot.help_command)
    bot.help_command = meme.MakeMemeCommand()
    bot.run()


if __name__ == "__main__":
    main()
