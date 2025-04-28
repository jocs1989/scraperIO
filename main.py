import asyncio
from crawl4ai import *
from src.cfg.browser_cfg import browser_conf
from src.strategy.base_strategy import config
from src.cfg.browser_cfg import browser_conf 
from src.cfg.dispatchers_cfg import dispatcher_semaphore as dispatcher
from src.strategy.base_strategy import config

async def main():

    urls=[f'https://www.vivanuncios.com.mx/s-venta-inmuebles/page-7/v1c1097p7',
          'https://www.vivanuncios.com.mx/s-venta-inmuebles/page-1/v1c1097p1' ]

    

    async with AsyncWebCrawler(config=browser_conf) as crawler:
        # Get all results at once
        results = await crawler.arun_many(
            urls=urls,
            config=config,
            dispatcher=dispatcher
        )

        
        for result in results:
            if result.success:
                dr = result.dispatch_result
                print(dr)
                print(result.extracted_content)
                print("="*20)
            else:
                print(f"Failed to crawl {result.url}: {result.error_message}")


if __name__ == "__main__":
    asyncio.run(main())
