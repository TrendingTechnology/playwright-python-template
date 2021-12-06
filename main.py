import asyncio
from time import sleep

import yaml
from playwright.async_api import Playwright, async_playwright

from chromium import get_executable_path

try:
    with open("config.yml") as f:
        CONFIG = yaml.load(f, Loader=yaml.SafeLoader)
except (FileNotFoundError, PermissionError):
    print("Config file not found or not accessible, starting with default options.")

global page


async def click(element: str, timeout: float | None = None) -> None:
    async with page.expect_navigation(timeout=timeout):
        await page.click(element)


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(
        headless=CONFIG["headless"],
        executable_path=get_executable_path(),
        args=CONFIG["chromium_args"],
    )
    context = await browser.new_context(viewport=None)

    global page
    page = await context.new_page()
    page.set_default_timeout(CONFIG["default_timeout"])

    await page.goto(CONFIG["start_page"])

    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
