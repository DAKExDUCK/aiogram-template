import datetime
from aiogram import types
import pytest

from unittest.mock import AsyncMock

from modules.bot.handlers.default import delete_msg, start, help
from modules.logger import Logger


@pytest.mark.asyncio
async def test_start():
    async def mock_send_message(text, reply_markup=None):
        assert text == "Start message"

        assert isinstance(reply_markup, types.InlineKeyboardMarkup)
        assert len(reply_markup.inline_keyboard) == 1
        assert len(reply_markup.inline_keyboard[0]) == 1
        button = reply_markup.inline_keyboard[0][0]
        assert button.text == "Delete"
        assert button.callback_data == "delete"

    message_mock = AsyncMock(reply=mock_send_message)

    await start(message_mock)


@pytest.mark.asyncio
async def test_help():
    async def mock_send_message(text, reply_markup=None):
        assert text == "Help message"

        assert isinstance(reply_markup, types.InlineKeyboardMarkup)
        assert len(reply_markup.inline_keyboard) == 1
        assert len(reply_markup.inline_keyboard[0]) == 1
        button = reply_markup.inline_keyboard[0][0]
        assert button.text == "Delete"
        assert button.callback_data == "delete"

    message_mock = AsyncMock(reply=mock_send_message)

    await help(message_mock)


@pytest.mark.asyncio
async def test_delete_msg_success():
    chat_id = 9
    message_id = 5
    chat = types.Chat(
        id=chat_id,
        type="private",
        username="AMD_RYZEN_5_9600X",
        first_name="JUST AMD RYZEN 5",
        last_name="9600X AM5 OEM",
    )
    reply_to_message = types.Message(
        message_id=message_id,
        date=datetime.datetime(2024, 6, 27, 5, 28, 32, tzinfo=datetime.timezone.utc),
        chat=chat,
        text="/start",
        entities=[
            types.MessageEntity(
                type="bot_command", offset=0, length=6, url=None, user=None, language=None, custom_emoji_id=None
            )
        ],
        forward_from_chat=chat,
        forward_sender_name="AMD RYZEN",
    )
    message = types.Message(
        message_id=message_id,
        date=datetime.datetime(2024, 6, 27, 5, 28, 32, tzinfo=datetime.timezone.utc),
        chat=chat,
        text="/start",
        entities=[
            types.MessageEntity(
                type="bot_command", offset=0, length=6, url=None, user=None, language=None, custom_emoji_id=None
            )
        ],
        reply_to_message=reply_to_message,
        forward_from_chat=chat,
        forward_sender_name="AMD RYZEN",
    )

    async def mock_delete_message(inner_chat_id, inner_message_id):
        assert inner_chat_id == chat_id
        assert inner_message_id == message_id
        print("mock called")

    async def answer_mock():
        pass

    bot = AsyncMock(delete_message=mock_delete_message)
    query_mock = AsyncMock(message=message, bot=bot, answer=answer_mock)

    await delete_msg(query_mock)


@pytest.mark.asyncio
async def test_delete_msg_error():
    Logger.load_config()
    chat_id = 9
    message_id = 5
    chat = types.Chat(
        id=chat_id,
        type="private",
        username="AMD_RYZEN_5_9600X",
        first_name="JUST AMD RYZEN 5",
        last_name="9600X AM5 OEM",
    )
    reply_to_message = types.Message(
        message_id=message_id,
        date=datetime.datetime(2024, 6, 27, 5, 28, 32, tzinfo=datetime.timezone.utc),
        chat=chat,
        text="/start",
        entities=[
            types.MessageEntity(
                type="bot_command", offset=0, length=6, url=None, user=None, language=None, custom_emoji_id=None
            )
        ],
        forward_from_chat=chat,
        forward_sender_name="AMD RYZEN",
    )
    message = types.Message(
        message_id=message_id,
        date=datetime.datetime(2024, 6, 27, 5, 28, 32, tzinfo=datetime.timezone.utc),
        chat=chat,
        text="/start",
        entities=[
            types.MessageEntity(
                type="bot_command", offset=0, length=6, url=None, user=None, language=None, custom_emoji_id=None
            )
        ],
        reply_to_message=reply_to_message,
        forward_from_chat=chat,
        forward_sender_name="AMD RYZEN",
    )

    async def mock_delete_message(_, __):
        raise Exception()

    async def answer_mock(msg):
        assert msg == "Error"

    bot = AsyncMock(delete_message=mock_delete_message)
    query_mock = AsyncMock(message=message, bot=bot, answer=answer_mock)

    await delete_msg(query_mock)
