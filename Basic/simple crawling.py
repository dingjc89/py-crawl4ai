import asyncio
from crawl4ai import AsyncWebCrawler


async def main():
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url="https://www.baidu.com",

      word_count_threshold=10,
      exclude_tags=['form', 'header'],
      exclude_external_links=True,

      process_iframe=True,
      remove_overlay_elements=True,

      timeout=10,
      bypass_cache=False,
      )

    if result.success:

      with open("baidu.html", "w", encoding="utf-8") as f:
        f.write(result.html)
      with open("baidu.md", "w", encoding="utf-8") as f:
        f.write(result.fit_markdown)

if __name__ == "__main__":
  asyncio.run(main())
