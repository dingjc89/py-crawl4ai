import asyncio
from crawl4ai import AsyncWebCrawler


async def main():
    proxy_config = {
        "server": "http://127.0.0.1:80",
        "username": "admin",
        "password": "admin",
    }

    async with AsyncWebCrawler(
            verbose=True,
            proxy_config=proxy_config,
    ) as crawler:
        result = await crawler.arun(url='http://ai.dev.com')


if __name__ == '__main__':
    asyncio.run(main())
