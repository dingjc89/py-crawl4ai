

import asyncio

from crawl4ai import AsyncWebCrawler


async def main():

  js_commands = [
      "document.querySelector('input').text('news');",
      "document.querySelector('input[type=submit]').click();",
  ]
  with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
       url="https://www.baidu.com",
       js_code= js_commands,
       delay_before_return_html=2.0,
       wait_for="css:.item:nth-child(10)",
       )
    print(result)

if __name__ == "__main__":
  asyncio.run(main())
