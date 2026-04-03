import os
import asyncio
from playwright.async_api import async_playwright
import glob

# We will read HTML files from `poster` directory
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'poster')

async def capture_posters():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Launch page with 1920x1080 resolution
        page = await browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)

        html_files = glob.glob(os.path.join(OUTPUT_DIR, '*.html'))
        for html_path in html_files:
            html_filename = os.path.basename(html_path)
            # User requested JPG format instead of PNG
            jpg_filename = html_filename.replace('.html', '.jpg')
            jpg_path = os.path.join(OUTPUT_DIR, jpg_filename)
            
            # Since HTMLs contain relative links like ../../website/assets,
            # We must load them via a local HTTP server served from `what_QI_want`
            html_url = f"http://localhost:8000/confirmed_speaker/poster/{html_filename}"
            
            print(f"Loading {html_url}...")
            # wait_until="networkidle" makes sure fonts and images load
            await page.goto(html_url, wait_until="networkidle")
            
            # Select the poster and save as JPEG with high quality
            poster_element = page.locator(".poster")
            print(f"Saving {jpg_filename}...")
            await poster_element.screenshot(path=jpg_path, type="jpeg", quality=95)
            print(f"✅ Saved: {jpg_filename}")

        await browser.close()
        print(f"🎉 All {len(html_files)} JPG posters generated in 16:9 format!")

if __name__ == '__main__':
    asyncio.run(capture_posters())
