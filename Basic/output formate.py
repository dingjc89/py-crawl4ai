import asyncio
import json
from crawl4ai import AsyncWebCrawler
from pydantic import BaseModel
from crawl4ai.extraction_strategy import LLMExtractionStrategy,JsonCssExtractionStrategy

class KnowledgeGraph(BaseModel):
  entities: list[dict]
  relationships: list[dict]


strategy = LLMExtractionStrategy(
  provider="ollama/llama3.2",
  schema=KnowledgeGraph.model_json_schema(),
  instruction="Extract entities and relationships from the content"
)

# async def main():
#   async with AsyncWebCrawler(verbose=True) as crawler:
#     result = await crawler.arun(url="http://www.baidu.com", extraction_strategy=strategy, instruction="Extract key information")


#     knowledge_graph = json.loads(result.extracted_content)

#     print(knowledge_graph)

async def css_main():
  scheme = {
    "name": "css selector",
    "baseSelector": "body",
    "fields": [
      {"name": "title", "selector": "title", "type": "text"},
      {"name": "news", "selector": "#s-top-left>a:first-child", "type": "text"},
      {"name": "hao123", "selector": "#s-top-left>a:last-child", "type": "text"},
    ]
  }

  strategy = JsonCssExtractionStrategy(scheme)
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(url="https://www.baidu.com", extraction_strategy=strategy)
    data = json.loads(result.extracted_content)
    print(data)



if __name__ == "__main__":
#   asyncio.run(main())
  asyncio.run(css_main())
