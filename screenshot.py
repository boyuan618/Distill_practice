import asyncio, datetime, os
from pyppeteer import launch


list_of_websites = ['https://main.scta.org.sg/', 'https://www.shodan.io/', 'http://scanme.nmap.org/']

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

    filename = f"screenshots/{newpath}/{datetime.datetime.now()}.png".replace(":", "_")
    await page.screenshot({'path': filename, 'fullPage': True})
    await browser.close()

    
#for website in list_of_websites:
for website in list_of_websites:
    asyncio.get_event_loop().run_until_complete(main(website))