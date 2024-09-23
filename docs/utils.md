# Directory: `C:/ticker/app/utils`

## File: `utils.py`

### Functions:

- **Function:** `format_feed_entry` (line 1)
  **Docstring:**
  ```
  Format a single feed entry into HTML.
  ```

:param entry: Feed entry from the RSS feed.
:return: Formatted HTML string.

````
```python
def format_feed_entry(entry):
  """
  Format a single feed entry into HTML.

  :param entry: Feed entry from the RSS feed.
  :return: Formatted HTML string.
  """
  return f"<li><a href='{entry.link}'>{entry.title}</a></li>"

````

<a href="/site_tickser/assets/utils.html" target="_blank">Click here to open the markmap file in a new tab</a>

<iframe src="/site_ticker/assets/utils.html" width="800" height="600"></iframe>
