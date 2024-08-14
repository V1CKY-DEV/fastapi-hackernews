from fastapi import FastAPI, HTTPException, Query
import httpx
from cachetools import TTLCache
import logging
import asyncio

app = FastAPI()

# Setting up a cache that keeps things stored for 10 minutes
cache = TTLCache(maxsize=100, ttl=600)

# Logging setup to keep track of whats happening
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/top-news")
async def get_top_news(count: int = Query(10, ge=1, le=50)):
    # Creating a key for our cache based on the number of stories requested
    cache_key = f"top-news-{count}"

    # Checking if we already have the result in the cache
    if cache_key in cache:
        logger.info("Fetching results from cache")
        return cache[cache_key]

    try:
        # Fetching top story IDs from Hacker News API
        async with httpx.AsyncClient() as client:
            response = await client.get("https://hacker-news.firebaseio.com/v0/topstories.json")
            response.raise_for_status()  # Will raise an error if the request failed
            story_ids = response.json()[:count]

            # Creating a list of tasks to get details for each story
            tasks = [client.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json") for story_id in story_ids]
            stories_responses = await asyncio.gather(*tasks)

            # Parsing each story’s response to JSON
            stories = [story.json() for story in stories_responses]

            # Storing the results in the cache
            cache[cache_key] = stories
            logger.info("Fetched and cached the top news successfully")

            return stories

    except httpx.HTTPStatusError as e:
        # Logging and handling HTTP errors, such as network issues or invalid responses
        logger.error(f"HTTP error occurred: {e.response.status_code}")
        raise HTTPException(status_code=e.response.status_code, detail="Error fetching data from Hacker News")
    except Exception as e:
        # Logging and handling any other unexpected errors
        logger.error(f"Something went wrong: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/")
def read_root():
    # Simple endpoint to check if the API is running
    return {"message": "Welcome to the Hacker News API"}
