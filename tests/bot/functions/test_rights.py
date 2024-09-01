import datetime

import pytest
from aiogram.types import Chat, Message, MessageEntity, User

from modules.bot.functions.rights import IsAdmin, is_Admin, is_admin

pytest_plugins = ("pytest_asyncio",)
chat = Chat(
    id=1072746639,
    type="private",
    title=None,
    username="AMD_RYZEN_5_9600X",
    first_name="JUST AMD RYZEN 5",
    last_name="9600X AM5 OEM",
)
user_adm = User(
    id=1072746639,
    is_bot=True,
    first_name="JUST AMD RYZEN 5",
    last_name="9600X AM5 OEM",
    username="AMD_RYZEN_5_9600X",
    language_code="en",
    is_premium=True,
)
user_not_adm = User(
    id=72746639,
    is_bot=True,
    first_name="JUST AMD RYZEN 5",
    last_name="9600X AM5 OEM",
    username="AMD_RYZEN_5_9600X",
    language_code="en",
    is_premium=True,
)
OUT = "admin funtionality"


@pytest.mark.asyncio
@pytest.mark.parametrize("user,exp", [(user_adm, OUT), (user_not_adm, None)])
async def test_is_decorator_admin(user, exp):
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

    @is_Admin
    async def some_func(_: Message) -> str:
        return exp

    assert await some_func(msg) == exp


@pytest.mark.parametrize(
    "user_id, exp", [(user_adm.id, True), (user_not_adm, False), (str(user_adm.id), True), (str(user_not_adm), False)]
)
def test_is_admin(user_id, exp):
    assert is_admin(user_id) == exp


@pytest.mark.asyncio
@pytest.mark.parametrize("user,exp", [(user_adm, True), (user_not_adm, False)])
async def test_is_admin_filter(user, exp):
    filter_is_admin = IsAdmin()
    msg = Message(
        message_id=7,
        date=datetime.datetime(2024, 6, 27, 5, 28, 32, tzinfo=datetime.timezone.utc),
        chat=chat,
        from_user=user,
        text="/start",
        entities=[
            MessageEntity(
                type="bot_command",
                offset=0,
                length=6,
            )
        ],
        forward_from=user,
        forward_from_chat=chat,
        forward_from_message_id=7,
        forward_sender_name="amd ryzen",
    )
    assert await filter_is_admin(msg) == exp
