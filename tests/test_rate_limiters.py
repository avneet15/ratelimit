from app.decorator import fixed_window_ratelimiter, sliding_log_ratelimiter
from app.exception import RequestRateLimited

# TEST FIXED WINDOW #
@fixed_window_ratelimiter(3, 5, 's')
def hello():
    return "Hello"


# TEST SLIDING LOG #
@sliding_log_ratelimiter(3, 10, 's')
def hello():
    return "Hello"

count = 0
while True:
    try:
        count += 1
        hello()
        print(count)

    except RequestRateLimited:
        pass







