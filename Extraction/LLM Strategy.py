import asyncio
import json

from crawl4ai.extraction_strategy import LLMExtractionStrategy
from pydantic import BaseModel
from tenacity import retry, stop_after_attempt, wait_exponential
from crawl4ai import AsyncWebCrawler


class Product(BaseModel):
    name: str
    price: float
    description: str


class LLMExtractionError(Exception):
    pass


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
async def extract_with_retry(crawler, url, extraction_strategy):
    try:
        result = await crawler.arun(url=url, extraction_strategy=extraction_strategy, bypass_cache=True)
        print(result.extracted_content)
    except Exception as e:
        raise LLMExtractionError(f"Failed to extract content: {str(e)}")


async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        strategy = LLMExtractionStrategy(
                provider="ollama/gemma2:27b",
                instruction="抓取产品名称、产品价格、产品描述内容，返回json格式为：[{'product_name':'ali product', 'product_price':19.99, "
                            "'product_description':'ali product description'}]",
                # instruction="获取分类下的商品信息、评论信息、相关商品信息等,并且返回的json格式为：[{\"category_name\":\"Electronics\","
                #             "\"products\":[{\"name\":\"Smartphone"
                #             "X\",\"price\":\"$999\",\"details\":{\"brand\":\"TechCorp\",\"model\":\"X-2000\"},"
                #             "\"features\":[{\"feature\":\"5G capable\"},{\"feature\":\"6.5\\\" OLED screen\"},"
                #             "{\"feature\":\"128GB storage\"}],\"reviews\":[{\"reviewer\":\"John D.\","
                #             "\"rating\":\"4.5\",\"comment\":\"Great phone, love the camera!\"},{\"reviewer\":\"Jane "
                #             "S.\",\"rating\":\"5\",\"comment\":\"Best smartphone I've ever owned.\"}],"
                #             "\"related_products\":[{\"name\":\"Phone Case\",\"price\":\"$29.99\"},{\"name\":\"Screen "
                #             "Protector\",\"price\":\"$9.99\"}]}]}]"
            )
        try:
            await extract_with_retry(crawler, "http://ai.dev.com/index.html", strategy)
        except LLMExtractionError as e:
            print(f"Extraction failed after retries: {e}")


if __name__ == '__main__':
    asyncio.run(main())
