# Directory: `C:/ticker/app/cache`

## File: `cache.py`

### Imports:

- import time
- from functools import wraps

### Functions:

- **Function:** `cache_result` (line 7)
  **Docstring:**
  ```
  Cache the result of a function for a specified time period.
  ```

:param time: Cache duration in seconds (default is 10 minutes).
:return: Wrapper function with caching applied.

````
```python
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

````

- **Function:** `decorator` (line 14)

  ```python
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

  ```

### Variables/Constants:

```python
cache = {}
```

```python
key = f"{func.__name__}_{args}_{kwargs}"
```

```python
result = await func(*args, **kwargs)
```

<a href="/site_ticker/assets/cache.html" target="_blank">Click here to open the markmap file in a new tab</a>

<iframe src="/site_ticker/assets/cache.html" width="800" height="600"></iframe>
