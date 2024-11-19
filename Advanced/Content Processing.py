import asyncio

from crawl4ai import AsyncWebCrawler


async def main():
    with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="http://www.baidu.com",
            excluded_tags=["form", "nav"]
        )
        print(result.cleaned_html)


if __name__ == '__main__':
    asyncio.run(main())
