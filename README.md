# News Ticker Service

A real-time news ticker service that fetches and displays programming-related content and general development news. Users can customize the feeds they want to see and the cache can be set between 1 to 10 minutes.

## Features

- Supports general development news and language-specific content (Python, JavaScript, Go).
- Cache system for performance, configurable from 1 to 10 minutes.
- Real-time fetching from multiple sources using RSS.

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repo/news-ticker-service.git
   cd news-ticker-service
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server**:

   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the ticker**:
   - Open your browser and navigate to `http://127.0.0.1:8000/ticker`.
   - You can pass query parameters to customize the feed (e.g., `?general_news=true&languages=python,javascript`).
