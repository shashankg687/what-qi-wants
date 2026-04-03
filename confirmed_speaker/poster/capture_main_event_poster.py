import os
import asyncio
from playwright.async_api import async_playwright

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

async def capture_main_poster():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Launch page with 1920x1080 resolution
        page = await browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)

        html_filename = "main_event_poster_16_9.html"
        jpg_filename = "main_event_poster.jpg"
        jpg_path = os.path.join(OUTPUT_DIR, jpg_filename)
        
        # We must load via HTTP server served from `what_QI_want`
        html_url = f"http://localhost:8000/confirmed_speaker/poster/{html_filename}"
        
        print(f"Loading {html_url}...")
        await page.goto(html_url, wait_until="networkidle")
        
        poster_element = page.locator(".poster")
        print(f"Saving {jpg_filename}...")
        await poster_element.screenshot(path=jpg_path, type="jpeg", quality=95)
        print(f"✅ Saved: {jpg_path}")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(capture_main_poster())
