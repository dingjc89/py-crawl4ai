import asyncio
import base64

from crawl4ai import AsyncWebCrawler

async def main():
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(url="https://www.baidu.com", screenshot=True, timeout=10, bypass_cache=True)
    print("++++++++++++++++++++++++++++++++++++++++++")
    if result.success and result.screenshot:
      screenshot_data = base64.b64decode(result.screenshot)
      with open("screenshot.png", "wb") as f:
        f.write(screenshot_data)

if __name__ == "__main__":
  asyncio.run(main())
