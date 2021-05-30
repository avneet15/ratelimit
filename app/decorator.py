from functools import wraps

from app.exception import RequestRateLimited
from app.ratelimiter import fixed_window_ratelimit
from app.ratelimiter import sliding_log_ratelimt


def fixed_window_ratelimiter(req_count, time_qty, granularity, redis_url="redis://localhost:6379/0"):
    def impl(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            is_ratelimited = fixed_window_ratelimit(req_count, time_qty, granularity, redis_url, func)
            if is_ratelimited:
                raise RequestRateLimited("Rate exceeded")
            return func(*args, **kwargs)
        return wrapper
    return impl


def sliding_log_ratelimiter(req_count, time_qty, granularity, redis_url="redis://localhost:6379/0"):
    def impl(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            is_ratelimited = sliding_log_ratelimt(req_count, time_qty, granularity, redis_url, func)
            if is_ratelimited:
                raise RequestRateLimited("Rate exceeded")
            return func(*args, **kwargs)
        return wrapper
    return impl