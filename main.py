import asyncio
from crawl4ai import *
from src.cfg.browser_cfg import browser_conf
from src.strategy.base_strategy import config


async def main():
    async with AsyncWebCrawler(config=browser_conf) as crawler:
        result = await crawler.arun(
            url="https://www.vivanuncios.com.mx/s-venta-inmuebles/v1c1097p1?utm_source=google&utm_medium=cpc&utm_campaign=Search_Brandterms&utm_content=Exact&gad_source=1",
            config=config
        )
        print(result.extracted_content)

if __name__ == "__main__":
    asyncio.run(main())
