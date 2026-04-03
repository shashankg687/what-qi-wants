import os
import asyncio
from playwright.async_api import async_playwright
import urllib.parse
from generate_speaker_posters import speakers

OUTPUT_DIR = "."

async def capture_posters():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1080, "height": 1080})

        for speaker in speakers:
            html_filename = speaker['filename']
            png_filename = html_filename.replace('.html', '.png')
            html_path = os.path.join(OUTPUT_DIR, html_filename)
            png_path = os.path.join(OUTPUT_DIR, png_filename)
            
            # Use localhost server to ensure assets load correctly
            html_url = f"http://localhost:8000/speakers/{html_filename}"
            
            print(f"Loading {html_url}...")
            await page.goto(html_url, wait_until="networkidle")
            
            # The poster has dimensions 1080x1080 and elements .poster
            # Select the poster explicitly to avoid capturing scrollbars
            poster_element = page.locator(".poster")
            print(f"Saving {png_filename}...")
            await poster_element.screenshot(path=png_path)
            print(f"✅ Saved: {png_filename}")

        await browser.close()
        print(f"\n🎉 All {len(speakers)} PNG posters generated!")

if __name__ == '__main__':
    asyncio.run(capture_posters())
