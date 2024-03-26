from webex_bot.models.command import Command
from webex_bot.models.response import Response, response_from_adaptive_card
from webexteamssdk.models.cards import (
    AdaptiveCard,
    Column,
    ColumnSet,
    FontSize,
    FontWeight,
    Text,
    TextBlock,
    Choice,
    Choices,
)
from webexteamssdk.models.cards.actions import Submit, OpenUrl

from app import img


TEMPLATES = img.get_templates()


class MakeMemeCommand(Command):
    """Class for initial Webex interactive card."""
    def __init__(self) -> None:
        super().__init__(
            command_keyword="/meme",
            help_message="Make a Meme",
            chained_commands=[MakeMemeCallback()],
            delete_previous_message=True,
        )

    def pre_execute(self, message, attachment_actions, activity) -> None:
        return

    def execute(self, message, attachment_actions, activity) -> Response:
        card_body: list = [
            ColumnSet(
                columns=[
                    Column(
                        width=1,
                        items=[
                            TextBlock(
                                "Make a Meme",
                                weight=FontWeight.BOLDER,
                                size=FontSize.MEDIUM,
                            ),
                            TextBlock(
                                "This bot uses memegen.link to generate memes. Click 'View Templates' to view available templates.",
                                weight=FontWeight.LIGHTER,
                                size=FontSize.SMALL,
                                wrap=True,
                            ),
                            TextBlock(
                                "Both fields are required. If you do not want to specify a value, please type a space.",
                                weight=FontWeight.LIGHTER,
                                size=FontSize.SMALL,
                                wrap=True,
                            ),
                        ],
                    ),
                ]
            ),
            ColumnSet(
                columns=[
                    Column(
                        width=1,
                        items=[
                            Choices(
                                id="meme_type",
                                isMultiSelect=False,
                                choices=[
                                    Choice(title=x["name"], value=x["choiceval"]) for x in TEMPLATES
                                ],
                            ),
                            Text(id="text_top", placeholder="Top Text", maxLength=100),
                            Text(
                                id="text_bottom",
                                placeholder="Bottom Text",
                                maxLength=100,
                            ),
                        ],
                    ),
                ]
            ),
        ]

        card: AdaptiveCard = AdaptiveCard(
            body=card_body,
            actions=[
                Submit(
                    title="Go!",
                    data={"callback_keyword": "make_meme_callback_rbamzfyx"},
                ),
                OpenUrl(url="https://memegen.link/#templates", title="View Templates"),
                Submit(title="Cancel", data={"command_keyword": "exit"}),
            ],
        )
        return response_from_adaptive_card(card)


class MakeMemeCallback(Command):
    """Class to process user data and return meme."""
    def __init__(self) -> None:
        super().__init__(
            card_callback_keyword="make_meme_callback_rbamzfyx",
            delete_previous_message=True,
        )
        self.error: bool = False
        self.text_top: str = ""
        self.text_bottom: str = ""
        self.meme: str = ""
        self.meme_filename: str = ""

    def pre_execute(self, message, attachment_actions, activity) -> str:
        self.meme: str = attachment_actions.inputs.get("meme_type")
        self.text_top: str = attachment_actions.inputs.get("text_top")
        self.text_bottom: str = attachment_actions.inputs.get("text_bottom")

        if not self.text_top and not self.text_bottom:
            self.error = True
            return "Please provide at least one positional text argument."

        if ".gif" in self.meme:
            return "Generating your meme. GIF-based memes take a little longer. Please wait..."

        return "Generating your meme..."

    def execute(self, message, attachment_actions, activity) -> Response | None:
        if self.error:
            return

        self.meme_filename: str = img.generate_api_url(
            self.meme, self.text_top, self.text_bottom
        )
        msg: Response = Response(
            attributes={
                "roomId": activity["target"]["globalId"],
                "parentId": "",
                "files": [self.meme_filename],
            }
        )
        return msg

    def post_execute(self, message, attachment_actions, activity) -> None:
        return
