#import playwright
import time
import playwright
# from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

# open browser and open google.com with await and async and sync and close the browser after 5 seconds
import asyncio
# from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.google.com")

        await page.wait_for_timeout(5000)  # Wait 5 seconds
        await browser.close()

asyncio.run(main())



# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.google.com")
#     time.sleep(5)
#     browser.close()
    

