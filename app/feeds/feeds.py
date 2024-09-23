import feedparser

FEEDS = {
    "general": ["https://news.ycombinator.com/rss", "https://dev.to/feed"],
    "languages": {
        "python": "https://realpython.com/atom.xml",
        "javascript": "https://javascriptweekly.com/rss",
        "golang": "https://golangweekly.com/rss",
    }
}

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
