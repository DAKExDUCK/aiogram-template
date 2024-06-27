import datetime

import pytest
from aiogram.types import Chat, Message, MessageEntity, User

from modules.bot.functions import functions

TEST_INPUT1 = "Chat id: `{clear_MD(message.forward_from_chat.id)}`"
EXPECTED1 = "Chat id: \`{clear\_MD\(message\.forward\_from\_chat\.id\)}\`"
TEST_INPUT2 = "*Star_something Venture Announces New Intake!*"
EXPECTED2 = "\*Star\_something Venture Announces New Intake!\*"
TEST_INPUT3 = "Register now: [click] (https://kazhackstan.com/)"
EXPECTED3 = "Register now: \[click\] \(https://kazhackstan\.com/\)"
TEST_INPUT4 = "~-~~---(())))"
EXPECTED4 = "\~\-\~\~\-\-\-\(\(\)\)\)\)"
TEST_INPUT5 = "some text without any md symbols"
EXPECTED5 = "some text without any md symbols"

chat = Chat(
    id=1072746639,
    type="private",
    title=None,
    username="AMD_RYZEN_5_9600X",
    first_name="JUST AMD RYZEN 5",
    last_name="9600X AM5 OEM",
)
user = User(
    id=1072746639,
    is_bot=True,
    first_name="JUST AMD RYZEN 5",
    last_name="9600X AM5 OEM",
    username="AMD_RYZEN_5_9600X",
    language_code="en",
    is_premium=True,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (TEST_INPUT1, EXPECTED1),
        (TEST_INPUT2, EXPECTED2),
        (TEST_INPUT3, EXPECTED3),
        (TEST_INPUT4, EXPECTED4),
        (TEST_INPUT5, EXPECTED5),
    ],
)
def test_clear_md(test_input, expected):
    assert functions.clear_MD(test_input) == expected


def test_get_info_from_forwarded_msg_1():
    msg = Message(
        message_id=7,
        date=datetime.datetime(2024, 6, 27, 5, 28, 32, tzinfo=datetime.timezone.utc),
        chat=chat,
        from_user=user,
        text="/start",
        entities=[
            MessageEntity(
                type="bot_command", offset=0, length=6, url=None, user=None, language=None, custom_emoji_id=None
            )
        ],
        forward_from=user,
        forward_from_chat=chat,
        forward_from_message_id=7,
        forward_sender_name="AMD RYZEN",
    )
    text, user_id, name, mention = functions.get_info_from_forwarded_msg(msg)
    expected_text = "Chat id: `1072746639`\n:star:\nBOT\nUser id: `1072746639`\nFull name: `JUST AMD RYZEN 5 9600X AM5 OEM`\nMention: @AMD\_RYZEN\_5\_9600X\nSender name: `AMD RYZEN`\nMsg id: `7`\n"
    assert text == expected_text
    assert user_id == 1072746639
    assert name == "JUST AMD RYZEN 5 9600X AM5 OEM"
    assert mention == "AMD_RYZEN_5_9600X"


def test_get_info_from_forwarded_msg_2():
    msg = Message(
        message_id=7,
        date=datetime.datetime(2024, 6, 27, 5, 28, 32, tzinfo=datetime.timezone.utc),
        chat=chat,
        text="/start",
        entities=[
            MessageEntity(
                type="bot_command", offset=0, length=6, url=None, user=None, language=None, custom_emoji_id=None
            )
        ],
        forward_from_chat=chat,
        forward_from_message_id=7,
        forward_sender_name="AMD RYZEN",
    )
    text, user_id, name, mention = functions.get_info_from_forwarded_msg(msg)
    expected_text = "Chat id: `1072746639`\nSender name: `AMD RYZEN`\nMsg id: `7`\n"
    assert text == expected_text
    assert user_id is None
    assert name is None
    assert mention is None
