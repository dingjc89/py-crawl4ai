import asyncio

from playwright.async_api import Browser, Page
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_crawler_strategy import AsyncPlaywrightCrawlerStrategy


async def on_browser_created(browser: Browser):
    print("[HOOK] on_browser_created")
    context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = await context.new_page()

    await page.goto('http://ai.dev.com')
    await page.fill('input[name="username"]', "admin")
    await page.fill('input[name="password"]', "admin")
    await page.click('input[type="submit"]')
    await page.wait_for_selector('#welcome')

    await page.close()
    await context.close()


async def before_goto(page: Page):
    print("[HOOK] before_goto")
    await page.set_extra_http_headers({'X-TEST-HEADER': 'text'})


async def after_goto(page: Page):
    print("[HOOK] after_goto")
    print(f"Current URL: {page.url}")


async def on_execution_started(page: Page):
    print("[HOOK] on_execution_started")
    await page.evaluate('console.log("Custom JS executed")')


async def before_return_html(page: Page, html: str):
    print("[HOOK] before_return_html")
    print(f"Page HTML: {len(html)}")
    return page


async def main():
    crawl_strategy = AsyncPlaywrightCrawlerStrategy(verbose=True)
    crawl_strategy.set_hook('on_browser_created', on_browser_created)
    crawl_strategy.set_hook('before_goto', before_goto)
    crawl_strategy.set_hook('after_goto', after_goto)
    crawl_strategy.set_hook('on_execution_started', on_execution_started)
    crawl_strategy.set_hook('before_return_html', before_return_html)

    async with AsyncWebCrawler(verbose=True, crawler_strategy=crawl_strategy) as crawler:
        result = await crawler.arun(
            url='http://ai.dev.com',
            js_code='window.scrollTo(0, document.body.scrollHeight)',
            wait_for="footer"
        )


if __name__ == "__main__":
    asyncio.run(main())
