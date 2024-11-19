import asyncio
import json

from bs4 import BeautifulSoup
from crawl4ai.extraction_strategy import LLMExtractionStrategy, JsonCssExtractionStrategy
from crawl4ai import AsyncWebCrawler
from pydantic import BaseModel, Field
from tenacity import retry, stop_after_attempt, wait_exponential

class Product(BaseModel):
    name: str = Field("name", description="Product name")
    price: float = Field("price", description="Product price")
    description: str = Field("Description", description="Product description")


strategy = LLMExtractionStrategy(
    provider="ollama/llama3.2",
    schema=Product.model_json_schema(),
    instruction="From the crawled content, extract all mentioned model names along with their"
                'One extracted model JSON format should look like this:{"name":"kevin","price":12.0,'
                '"description":"Awesome product description"}',
)


async def main():
    # schema = {
    #     "name": "demo",
    #     "baseSelector": ".product",
    #     "fields": [
    #         {"name": "name", "type": "text", "selector": ".name"},
    #         {"name": "price", "type": "text", "selector": ".price"},
    #         {"name": "description", "type": "text", "selector": ".description"},
    #     ],
    # }
    #
    # strategy = JsonCssExtractionStrategy(schema, verbose=True)
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="http://ai.dev.com",
            extraction_strategy=strategy,
        )
        print(result.extracted_content)


if __name__ == "__main__":
    asyncio.run(main())
