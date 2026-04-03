import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1080, "height": 1080})
        await page.goto("http://localhost:8000/dwave_problem.html", wait_until="networkidle")
        await page.screenshot(path="dwave_problem_preview.png", full_page=True)
        await browser.close()
        print("Done")

asyncio.run(capture())
