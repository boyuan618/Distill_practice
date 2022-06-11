import asyncio, datetime, os
from pyppeteer import launch


list_of_websites = ['https://www.iiss.org/events/shangri-la-dialogue/shangri-la-dialogue-2022']

async def main(website):
    browser = await launch(headless=True)
    page = await browser.newPage()

    await page.goto(website, waitUntil="load")
    
    print(website)
    newpath = website.replace("https://", "").replace("http://", "")
    newpath = newpath.replace("/", "_").strip("_")
    print(newpath)
    if not os.path.exists("screenshots/" + newpath):
        os.makedirs("screenshots/" + newpath)
        
    if not os.path.exists("defacement/" + newpath):
        os.makedirs("defacement/" + newpath)

    filename = f"screenshots/{newpath}/{datetime.datetime.now()}.png".replace(":", "_")
    await page.screenshot({'path': filename, 'fullPage': True})
    await browser.close()

    
#for website in list_of_websites:
for website in list_of_websites:
    asyncio.get_event_loop().run_until_complete(main(website))