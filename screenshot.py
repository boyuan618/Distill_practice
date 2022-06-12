import asyncio, datetime, os
from pyppeteer import launch


list_of_websites = ['http://shielded-harbor-71309.herokuapp.com/login-pc']

async def main(website):
    browser = await launch(headless=True)
    page = await browser.newPage()

    await page.goto(website, waitUntil="load")
    
    
    #Creates folders if this is a new webpage
    newpath = website.replace("https://", "").replace("http://", "")
    newpath = newpath.replace("/", "_").strip("_")
    if not os.path.exists("screenshots/" + newpath):
        os.makedirs("screenshots/" + newpath)
        os.makedirs("screenshots/" + newpath + "/html")
        os.makedirs("screenshots/" + newpath + "/content")
        os.makedirs("screenshots/" + newpath + "/images")
        
    if not os.path.exists("defacement/" + newpath):
        os.makedirs("defacement/" + newpath)
        os.makedirs("defacement/" + newpath + "/html")
        os.makedirs("defacement/" + newpath + "/content")
        os.makedirs("defacement/" + newpath + "/images")


    #Scraping of website
    filename = f"screenshots/{newpath}/images/{datetime.datetime.now()}.png".replace(":", "_")
    await page.screenshot({'path': filename, 'fullPage': True}) #Screenshot page
    textcontent = await page.evaluate('document.body.textContent', force_expr=True) #Scraping textcontent
    html = await page.content() #Scraping html 
    
    #Writing scraped content into files
    with open(f"screenshots\\{newpath}\\content\\{datetime.datetime.now()}.txt".replace(":", "_"), "w+") as file:
        file.write(textcontent)
    
    with open(f"screenshots\\{newpath}\\html\\{datetime.datetime.now()}.html".replace(":", "_"), "w+") as file:
        file.write(html)
        
    await browser.close()

    
#for website in list_of_websites:
for website in list_of_websites:
    asyncio.get_event_loop().run_until_complete(main(website))