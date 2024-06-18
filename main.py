from aiohttp import *
import asyncio

async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return text
    

async def main():
    task1 = asyncio.create_task(fetch("https://googleplex.com"))
    result = await asyncio.gather(task1)
    print(result)


if __name__ == '__main__'
asyncio.run(main())