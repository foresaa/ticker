# Directory: `C:/ticker/app`

## File: `main.py`

### Imports:

- from fastapi import FastAPI, Query
- from fastapi.responses import HTMLResponse
- from app.feeds import fetch_feeds
- from app.cache import cache_result
- from fastapi.staticfiles import StaticFiles

### Variables/Constants:

```python
app = FastAPI()
```

```python
feeds = fetch_feeds(general_news, languages)
```

<a href = "/site_ticker/assets/app.html" target = "_blank">Click here to open the markmap file in a new tab</a>

<iframe src="/site_ticker/assets/app.html" width="800" height="600"></iframe>
