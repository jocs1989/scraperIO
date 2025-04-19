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


class BrowserConfig(BaseSettings):
    BROWSER_TYPE: str =  BrowserType.CHROMIUM.value
    BROWSER_HEADLESS: bool = True
    BROWSER_PROXY_CONFIG: Optional[Union[ProxyConfig, Dict, None]] = None
    BROWSER_VIEWPORT_WIDTH: int = 1080
    BROWSER_VIEWPORT_HEIGHT: int = 600
    BROWSER_VERBOSE: bool = True
    BROWSER_USE_PERSISTENT_CONTEXT: bool = False 
    BROWSER_COOKIES: Optional[List[Dict]] = None
    BROWSER_HEADERS: Optional[Dict[str, str]] = None
    BROWSER_USER_AGENT: str = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/116.0.0.0 Safari/537.36"
    BROWSER_TEXT_MODE: bool = False
    BROWSER_LIGHT_MODE: bool = False    
    BROWSER_EXTRA_ARGS: Optional[List[str]] = None


# Base Config class to load environment variables
class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# GlobalConfig: Basic config that will be used in all environments
class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False


# Different configurations based on environment
class DevConfig(GlobalConfig):
    HEADLESS: bool = False
    VERBOSE: bool = True
    model_config = SettingsConfigDict(env_prefix="DEV_")


class ProdConfig(GlobalConfig):
    HEADLESS: bool =True
    VERBOSE: bool = False
    model_config = SettingsConfigDict(env_prefix="PROD_")


class TestConfig(GlobalConfig):
    DATABASE_URL: str = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True
    model_config = SettingsConfigDict(env_prefix="TEST_")


@lru_cache()
def get_config(env_state: str):
    """Instantiate config based on the environment."""
    configs = {"dev": DevConfig, "prod": ProdConfig, "test": TestConfig}
    return configs[env_state]()


# Load environment state and get the corresponding config
config = get_config(BaseConfig().ENV_STATE)

# Example: Print loaded config (BrowserConfig)
print(config.dict())  # Imprimir la configuración cargada
