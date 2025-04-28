from crawl4ai import RateLimiter,CrawlerMonitor, DisplayMode

#https://docs.crawl4ai.com/advanced/multi-url-crawling/
# Create a RateLimiter with custom settings
rate_limiter = RateLimiter(
    base_delay=(0.5, 4),  # Random delay between 2-4 seconds
    max_delay=30.0,         # Cap delay at 30 seconds
    max_retries=10,          # Retry up to 5 times on rate-limiting errors
    rate_limit_codes=[429, 503]  # Handle these HTTP status codes
)


monitor = CrawlerMonitor(
    # Maximum rows in live display
    


)

