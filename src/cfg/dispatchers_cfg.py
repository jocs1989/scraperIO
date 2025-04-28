from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher,SemaphoreDispatcher
from src.cfg.core_cfg import rate_limiter,monitor


dispatcher_memory_adaptive = MemoryAdaptiveDispatcher(
    memory_threshold_percent=90.0,  # Pause if memory exceeds this
    check_interval=1.0,             # How often to check memory
    max_session_permit=10,          # Maximum concurrent tasks
    rate_limiter=rate_limiter,
    monitor=monitor
)


dispatcher_semaphore = SemaphoreDispatcher(
    semaphore_count=10,
    max_session_permit=5,         # Maximum concurrent tasks
    rate_limiter=rate_limiter,
    monitor=monitor
)
