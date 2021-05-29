from app.decorator import ratelimiter
from app.exception import RequestRateLimited


@ratelimiter(10, 15, 's')
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







