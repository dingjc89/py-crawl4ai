import asyncio
import json

from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy


async def main():
    schema = {
        "fields": [
            {"name": "name", "type": "text", "selector": "h1.product"},
            {"name": "price", "type": "text", "selector": "span.price"},
            {"name": "description", "type": "text", "selector": "p.description"},
        ]
    }
    strategy = JsonCssExtractionStrategy(schema)
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="http://ai.dev.com",
            extraction_strategy=strategy,
        )
        print(json.loads(result.extracted_content))


if __name__ == '__main__':
    asyncio.run(main())
