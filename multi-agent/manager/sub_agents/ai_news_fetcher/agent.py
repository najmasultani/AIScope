from google.adk.agents import Agent
from google.adk.tools import google_search

ai_news_fetcher = Agent(
    name="ai_news_fetcher",
    model="gemini-2.0-flash",
    description="News analyst agent",
    instruction="""
    You are a helpful assistant that can analyze news articles and provide a summary of the news.

    When asked about news, you should use the google_search tool to search for the news.

    If the user ask for news using a relative time, you should use the get_current_time tool to get the current time to use in the search query.
    """,
    tools=[google_search],
)
