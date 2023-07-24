from webex_bot.models.command import Command


class ExitCommand(Command):
    def __init__(self) -> None:
        super().__init__(
            command_keyword="exit",
            help_message="Exit",
            delete_previous_message=True,
        )
        self.sender: str = ""

    def pre_execute(self, message, attachment_actions, activity) -> None:
        return

    def execute(self, message, attachment_actions, activity) -> None:
        return

    def post_execute(self, message, attachment_actions, activity) -> None:
        return
