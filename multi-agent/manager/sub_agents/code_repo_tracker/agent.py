from datetime import datetime
from google.adk.agents import Agent
import requests


def search_github_tool(query: str) -> dict:
    """
    Searches GitHub for trending repositories based on a query string.
    This is a simplified custom tool using GitHub's public search API.
    """
    print(f"--- Tool: search_github_tool called with query: {query} ---")
    try:
        headers = {"Accept": "application/vnd.github.v3+json"}
        params = {"q": query, "sort": "stars", "order": "desc", "per_page": 5}
        response = requests.get("https://api.github.com/search/repositories", headers=headers, params=params)

        if response.status_code != 200:
            return {
                "status": "error",
                "error_message": f"GitHub API error: {response.status_code} - {response.text}"
            }

        data = response.json()
        results = [
            {
                "name": item["name"],
                "url": item["html_url"],
                "description": item.get("description", ""),
                "stars": item.get("stargazers_count", 0),
            }
            for item in data.get("items", [])
        ]

        return {
            "status": "success",
            "query": query,
            "results": results,
            "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error searching GitHub: {str(e)}",
        }


# Create the code_repo_tracker agent
code_repo_tracker = Agent(
    name="code_repo_tracker",
    model="gemini-2.0-flash",
    description="Tracks trending AI code and research tools from GitHub, arXiv, and HuggingFace.",
    instruction="""
    You are an agent specialized in discovering trending AI tools, code libraries, and model updates.

    Use the available tools to:
    - Track trending GitHub repositories by stars and relevance.
    - Retrieve recent research papers from arXiv (cs.AI, cs.LG).
    - Fetch latest models from HuggingFace (e.g., Llama, Stable Diffusion, etc.).

    Example user queries:
    - "Show me trending AI libraries on GitHub"
    - "Any new models on HuggingFace?"
    - "What are the latest papers on LLMs from arXiv?"

    Summarize each finding clearly, with links and short descriptions.
    """,
    tools=[search_github_tool],
)
