

from crawl4ai import AsyncWebCrawler


async def main():
  with AsyncWebCrawler(
    verbose=True,
    headless=True,

    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    },
    # proxy = "http://127.0.0.1:8080",
    ) as crawler:
        result = await crawler.arun(
            url="https://www.baidu.com",
            timeout=10,
            bypass_cache=True,
            process_iframe=True,
            screenshot=True,

            page_timeout=60000,
            delay_before_return_html=2.0,

            js_code= [
                "window.scrollTo(0, document.body.scrollHeight);",
                "document.querySelector('.load-more')?.click();",
            ],
            wait_for="css:.dynamic-content"
        )



