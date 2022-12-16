import asyncio
import re
import sys

from pyppeteer import launch


async def create_screenshot(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    file_name = re.sub(r'[^0-9a-z]+', r'-', url.lower())
    await page.screenshot({'path': f'{file_name}.png'})
    await browser.close()


if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://pybit.es'
    asyncio.get_event_loop().run_until_complete(
        create_screenshot(url))