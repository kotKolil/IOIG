from settings import *

from aiohttp import web, ClientSession
import asyncio
from bs4 import BeautifulSoup as bsf

async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return text
    
def get_url_img(text:str):
    text = bsf(text, "lxml")
    a = text.find("img", {"class":"login-image"})
    return a["src"]

async def index(request):
    text = await fetch("https://googleplex.com") 
    img_url = get_url_img(text)
    q = await fetch(img_url)
    return web.Response(text= q.read_bytes() , content_type="image/png")

async def main():
    task1 = asyncio.create_task(fetch("https://googleplex.com"))
    result = await asyncio.gather(task1)
    print(result)


async def main():
    app = web.Application()
    app.add_routes(
        [
            web.get('/', index)
         ]
        )

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, host, port)

    await site.start()

    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())