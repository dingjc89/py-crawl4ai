import asyncio
from crawl4ai import AsyncWebCrawler
from pydantic import BaseModel
from typing import List
from crawl4ai.extraction_strategy import LLMExtractionStrategy
import os


class Entity(BaseModel):
  name:str
  description: str


class Relationship(BaseModel):
  entity1: Entity
  entity2: Entity
  relationship_type: str
  description: str

class KnowledgeGraph(BaseModel):
  entities: List[Entity]
  relationships: List[Relationship]

extraction_strategy = LLMExtractionStrategy(
  provider="openai/gpt-3.5-turbo",
  api_token = os.getenv("OPENAI_API_KEY"),
  schema=KnowledgeGraph.model_json_schema(),
  extraction_type="schema",
  instructions="Extract the knowledge graph from the given text."
)

async def main():
 with AsyncWebCrawler(verbose=True) as crawler:
  result = await crawler.arun(url="https://www.baidu.com", extraction_strategy=extraction_strategy, timeout=10, bypass_cache=True)


if __name__ == "__main__":
  asyncio.run(main())
