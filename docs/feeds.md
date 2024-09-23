# Directory: `C:/ticker/app/feeds`

## File: `feeds.py`

### Imports:

- import feedparser

### Functions:

- **Function:** `fetch_feeds` (line 12)
  **Docstring:**
  ```
  Fetch the feeds from various programming-related sources.
  ```

:param include_general: Whether to include general development news.
:param languages: Comma-separated list of programming languages.
:return: List of feed entries.

````
```python
def fetch_feeds(include_general: bool, languages: str):
  """
  Fetch the feeds from various programming-related sources.

  :param include_general: Whether to include general development news.
  :param languages: Comma-separated list of programming languages.
  :return: List of feed entries.
  """
  feeds_to_fetch = []

  if include_general:
      feeds_to_fetch.extend(FEEDS["general"])

  if languages:
      for lang in languages.split(","):
          if lang in FEEDS["languages"]:
              feeds_to_fetch.append(FEEDS["languages"][lang])

  feed_entries = []
  for feed_url in feeds_to_fetch:
      feed = feedparser.parse(feed_url)
      feed_entries.extend(feed.entries)

  return feed_entries

````

### Variables/Constants:

```python
FEEDS = {
  "general": ["https://news.ycombinator.com/rss", "https://dev.to/feed"],
  "languages": {
      "python": "https://realpython.com/atom.xml",
      "javascript": "https://javascriptweekly.com/rss",
      "golang": "https://golangweekly.com/rss",
  }
}
```

```python
feeds_to_fetch = []
```

```python
feed_entries = []
```

```python
feed = feedparser.parse(feed_url)
```

<a href="/assets/feeds.html" target="_blank">Click here to open the markmap file in a new tab</a>

<iframe src="/assets/feeds.html" width="800" height="600"></iframe>
