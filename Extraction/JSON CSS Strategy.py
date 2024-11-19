import asyncio
import json

from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy


async def main():
    schema = {
        "name": "E-commerce Product Catalog",
        "baseSelector": "div.category",
        "fields": [
            {
                "name": "category_name",
                "selector": "h2.category-name",
                "type": "text"
            },
            {
                "name": "products",
                "selector": "div.product",
                "type": "nested_list",
                "fields": [
                    {
                        "name": "name",
                        "selector": "h3.product-name",
                        "type": "text"
                    },
                    {
                        "name": "price",
                        "selector": "p.product-price",
                        "type": "text"
                    },
                    {
                        "name": "details",
                        "selector": "div.product-details",
                        "type": "nested",
                        "fields": [
                            {
                                "name": "brand",
                                "selector": "span.brand",
                                "type": "text"
                            },
                            {
                                "name": "model",
                                "selector": "span.model",
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "name": "features",
                        "selector": "ul.product-features li",
                        "type": "list",
                        "fields": [
                            {
                                "name": "feature",
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "name": "reviews",
                        "selector": "div.review",
                        "type": "nested_list",
                        "fields": [
                            {
                                "name": "reviewer",
                                "selector": "span.reviewer",
                                "type": "text"
                            },
                            {
                                "name": "rating",
                                "selector": "span.rating",
                                "type": "text"
                            },
                            {
                                "name": "comment",
                                "selector": "p.review-text",
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "name": "related_products",
                        "selector": "ul.related-products li",
                        "type": "list",
                        "fields": [
                            {
                                "name": "name",
                                "selector": "span.related-name",
                                "type": "text"
                            },
                            {
                                "name": "price",
                                "selector": "span.related-price",
                                "type": "text"
                            }
                        ]
                    }
                ]
            }
        ]
    }
    schema = {
        "name": "products",
        "baseSelector": "div.product",
        "type": "nested_list",
        "fields": [
            {
                "name": "name",
                "type": "text",
                "selector": ".name"
            },
            {
                "name": "price",
                "type": "text",
                "selector": ".price"
            },
            {
                "name": "description",
                "type": "text",
                "selector": ".description"
            },

        ]
    }
    strategy = JsonCssExtractionStrategy(
        schema=schema,
    )
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="http://ai.dev.com/index.html",
            extraction_strategy=strategy,
            # browser_type="firefox" # chromium, firefox, webkit
        )
        print(result.extracted_content)
        product_data = json.loads(result.extracted_content)
        print(product_data)


if __name__ == '__main__':
    asyncio.run(main())
