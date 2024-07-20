import asyncio
import json
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

import redis.asyncio as redis

from valuta import baba
import config

dp = Dispatcher()
r = redis.Redis(host=config.HOST, port=config.PORT, decode_responses=True)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(F.text.startswith("/rates"))
async def rates(message: Message) -> None:
    text = ""
    data = await r.hgetall("data")
    for i in data:
        valuta_data = json.loads(data[i])
        text += f"{valuta_data['name']}({valuta_data['charcode']})=={valuta_data['value']} rubles\n"

    await message.answer(text)


@dp.message(F.text.startswith("/exchange"))
async def exchange(message: Message) -> None:
    x = message.text.split(" ")
    if len(x) < 4:
        await message.answer("чета не то")
    v1 = x[1]
    v2 = x[2]

    try:
        if v1 == "RUB":
            v1 = 1
        else:
            v1_data = json.loads(await r.hget("data", v1))
            v1 = int(v1_data["value"])

        if v2 == "RUB":
            v2 = 1
        else:
            v2_data = json.loads(await r.hget("data", v2))
            v2 = int(v2_data["value"])

        amount = int(x[3])
    except Exception as ex:
        print(ex)
        await message.answer("чета не то")
        return

    await message.answer(f"{v1/v2 * amount}")


async def main() -> None:
    bot = Bot(token=config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await asyncio.gather(dp.start_polling(bot), baba())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
