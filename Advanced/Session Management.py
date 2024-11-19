import asyncio
from crawl4ai import AsyncWebCrawler


async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        try:
            session_id = "my_session"
            result1 = await crawler.arun(
                url="http://ai.dev.com/page1",
                session_id=session_id,
            )
            result2 = await crawler.arun(
                url="http://ai.dev.com/page2",
                session_id=session_id,
            )
            result2 = await crawler.arun(
                url="http://ai.dev.com/page3",
                session_id=session_id,
            )
        finally:
            await crawler.crawler_strategy.kill_session(session_id)


if __name__ == '__main__':
    asyncio.run(main())
