def format_feed_entry(entry): 
    """
    Format a single feed entry into HTML.
    
    :param entry: Feed entry from the RSS feed.
    :return: Formatted HTML string.
    """
    return f"<li><a href='{entry.link}'>{entry.title}</a></li>"
