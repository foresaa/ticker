import time
from functools import wraps

# A simple cache dictionary
cache = {}

def cache_result(time=600):
    """
    Cache the result of a function for a specified time period.
    
    :param time: Cache duration in seconds (default is 10 minutes).
    :return: Wrapper function with caching applied.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = f"{func.__name__}_{args}_{kwargs}"
            if key in cache:
                result, timestamp = cache[key]
                if time.time() - timestamp < time:
                    return result
            
            result = await func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result
        
        return wrapper
    return decorator
