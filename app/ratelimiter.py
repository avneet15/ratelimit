import redis

GRANULARITY_CONVERTER = {
    's': 1,
    'm': 60,
    'h': 60*60,
    'd': 24*60*60
}


def ratelimit(req_count, time_qty, granularity, redis_url, func):
    r = redis.from_url(redis_url)

    time_window_in_sec = time_qty * GRANULARITY_CONVERTER[granularity]

    key = f"{func.__name__}_10"

    v = r.get(key)

    if v:
        current_count = int(v.decode('utf-8'))
        if current_count >= req_count:
            return True

    new_value = r.incr(key)
    #print(f"Redis key: {new_value}")
    if new_value == 1:
        r.expire(key, time_window_in_sec)

    return False
