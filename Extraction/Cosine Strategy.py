import asyncio

from crawl4ai.extraction_strategy import CosineStrategy
from crawl4ai import AsyncWebCrawler

strategy = CosineStrategy(
    semantic_filter="product reviews",
    word_count_threshold=20,
    sim_threshold=0.4,
    top_k=10
)


async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="http://ai.dev.com",
            extraction_strategy=strategy
        )
        print(result.extracted_content)


if __name__ == "__main__":
    asyncio.run(main())
