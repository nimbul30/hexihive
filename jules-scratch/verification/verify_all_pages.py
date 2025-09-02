import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Get the absolute path to the HTML files
        base_path = os.path.abspath('.')

        # 1. Navigate to home.html and take a screenshot
        await page.goto(f"file://{base_path}/home.html")
        await page.screenshot(path="jules-scratch/verification/01_home.png")

        # 2. Click "Connect Wallet" and go to setup.html
        await page.get_by_role("link", name="Connect Wallet").click()
        await page.wait_for_url(f"file://{base_path}/setup.html")
        await page.screenshot(path="jules-scratch/verification/02_setup.png")

        # 3. Navigate to news.html and take a screenshot
        await page.goto(f"file://{base_path}/news.html")
        await page.screenshot(path="jules-scratch/verification/03_news.png")

        # 4. Click the first story and go to insidehexi.html
        await page.get_by_role("link", name="Global Tech Summit Highlights Breakthroughs in AI and Sustainability").click()
        await page.wait_for_url(f"file://{base_path}/insidehexi.html")
        await page.screenshot(path="jules-scratch/verification/04_insidehexi.png")

        # 5. Navigate to userdash.html and take a screenshot
        await page.goto(f"file://{base_path}/userdash.html")
        await page.screenshot(path="jules-scratch/verification/05_userdash.png")

        # 6. Navigate to comb.html and take a screenshot
        await page.goto(f"file://{base_path}/comb.html")
        await page.screenshot(path="jules-scratch/verification/06_comb.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
