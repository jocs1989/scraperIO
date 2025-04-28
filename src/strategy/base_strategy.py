from crawl4ai import CrawlerRunConfig,CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from config import config

# https://docs.crawl4ai.com/core/content-selection/

# ajustar a necesidades de scraper
schema = {
        "name": "News Items",
        "baseSelector": ".postingCard-module__posting-top",
        "fields": [
            {"name": "location",
              "selector": ".postingLocations-module__location-block",
                "type": "text"},
                 {"name": "price",
              "selector": ".postingPrices-module__price",
                "type": "text"},{"name": "postingLocation",
              "selector": ".postingLocations-module__location-text",
                "type": "text"},{
            "name": "features",
            "selector": "[data-qa='POSTING_CARD_FEATURES']",
            "type": "text"
        },
            
        ]
    }

extraction_strategy= JsonCssExtractionStrategy(schema)


config   = CrawlerRunConfig(

    extraction_strategy=extraction_strategy
)
