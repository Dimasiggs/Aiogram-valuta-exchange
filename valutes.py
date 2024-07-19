from asyncio import sleep
import json
import redis.asyncio as redis

import aiohttp
from xml.etree import ElementTree as Etree

import config

r = redis.Redis(host=config.HOST, port=config.PORT, decode_responses=True)


async def baba():
    while 1:
        xml_data = await get_xml(config.URL)
        dict_data = await xml_to_dict(xml_data)

        for i in dict_data:
            await r.hset("data", i["charcode"], json.dumps(i))

        print("data updated!")
        await sleep(60*60*24)


async def get_xml(url) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def xml_to_dict(data: str) -> list:
    valutes = []
    root = Etree.fromstring(data)
    for valute in root:
        value = None
        charcode = None
        name = None
        for i in valute:
            if i.tag == "VunitRate":
                value = float(i.text.replace(",", "."))
            elif i.tag == "CharCode":
                charcode = i.text
            elif i.tag == "Name":
                name = i.text
        valutes.append({"charcode": charcode, "value": value, "name": name})

    return valutes
