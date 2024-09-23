from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from app.feeds import fetch_feeds
from app.cache import cache_result
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the static directory for serving CSS or JS files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/ticker", response_class=HTMLResponse)
@cache_result(time=600)  # Cache results for 10 minutes
async def get_ticker(
    general_news: bool = Query(True, description="Include general development news"),
    languages: str = Query(None, description="Comma-separated list of programming languages")
):
    """
    Endpoint to fetch the news ticker based on user preferences.
    
    :param general_news: Include general development news if True.
    :param languages: Comma-separated list of programming languages.
    :return: HTML response containing the ticker.
    """
    feeds = fetch_feeds(general_news, languages)
    return app.templates.TemplateResponse("ticker.html", {"request": {}, "feeds": feeds})
