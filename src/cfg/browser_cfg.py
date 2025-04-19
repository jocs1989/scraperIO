from crawl4ai import BrowserConfig
from config import config


browser_conf = BrowserConfig(
    browser_type=config.BROWSER_TYPE,
    headless=config.BROWSER_HEADLESS,
    proxy_config=config.BROWSER_PROXY_CONFIG,
    viewport_width=config.BROWSER_VIEWPORT_WIDTH,
    viewport_height=config.BROWSER_VIEWPORT_HEIGHT,
    verbose=config.BROWSER_VERBOSE,
    use_persistent_context=config.BROWSER_USE_PERSISTENT_CONTEXT,
    cookies=config.BROWSER_COOKIES,
    headers=config.BROWSER_HEADERS,
    user_agent=config.BROWSER_USER_AGENT,
    text_mode=config.BROWSER_TEXT_MODE,
    light_mode=config.BROWSER_LIGHT_MODE,
    browser_mode=config.BROWSER_EXTRA_ARGS,
)
