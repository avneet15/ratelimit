from functools import wraps

from app.exception import RequestRateLimited
from app.ratelimiter import ratelimit


def ratelimiter(req_count, time_qty, granularity, redis_url="redis://localhost:6379/0"):
    def impl(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            is_ratelimited = ratelimit(req_count, time_qty, granularity, redis_url, func)
            if is_ratelimited:
                raise RequestRateLimited("Rate exceeded")
            return func(*args, **kwargs)
        return wrapper
    return impl
