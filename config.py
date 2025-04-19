from functools import lru_cache
from typing import Optional, Union, List, Dict
from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum

class BrowserType(str, Enum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    SAFARI = "safari"

class ProxyConfig(BaseSettings):
    proxy_url: str
    username: Optional[str] = None
    password: Optional[str] = None


class DockerConfig(BaseSettings):
    image: str
    container_name: Optional[str] = None
    ports: Optional[Dict[str, str]] = None




# Base Config class to load environment variables
class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")





# GlobalConfig: Basic config that will be used in all environments
class GlobalConfig(BaseConfig):
    BROWSER_TYPE: str =  "chromium"
    BROWSER_HEADLESS: bool = True
    BROWSER_PROXY_CONFIG: Optional[Union[ProxyConfig, Dict, None]] = None
    BROWSER_VIEWPORT_WIDTH: int = 1080
    BROWSER_VIEWPORT_HEIGHT: int = 600
    BROWSER_VERBOSE: bool = True
    BROWSER_USE_PERSISTENT_CONTEXT: bool = False 
    BROWSER_COOKIES: Optional[Union[ Dict, None]] = None
    BROWSER_HEADERS: Optional[Union[ Dict, None]] = None
    BROWSER_USER_AGENT: Optional[Union[ str, None]] =  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/116.0.0.0 Safari/537.36"
    BROWSER_TEXT_MODE: bool = True
    BROWSER_LIGHT_MODE: bool = True    
    BROWSER_EXTRA_ARGS: Optional[Union[ str, None]]= None


# Different configurations based on environment
class DevConfig(GlobalConfig):
    BROWSER_HEADLESS: bool = False
    BROWSER_VERBOSE: bool = True
    model_config = SettingsConfigDict()


class ProdConfig(GlobalConfig):
    BROWSER_HEADLESS: bool = True
    BROWSER_VERBOSE: bool = False
    model_config = SettingsConfigDict()


class TestConfig(GlobalConfig):
  
    model_config = SettingsConfigDict()


@lru_cache()
def get_config(env_state: str):
    """Instantiate config based on the environment."""
    configs = {"dev": DevConfig, "prod": ProdConfig, "test": TestConfig}
    return configs[env_state]()


# Load environment state and get the corresponding config
config = get_config(BaseConfig().ENV_STATE)

