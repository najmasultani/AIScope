from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

# Sub-agents
from .sub_agents.code_repo_tracker.agent import code_repo_tracker
from .sub_agents.code_tester.agent import code_tester
from .sub_agents.ai_news_fetcher.agent import ai_news_fetcher
from .sub_agents.insight_summarizer.agent import insight_summarizer
from .tools.tools import get_current_time

# Root manager agent
root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent that delegates or coordinates AI-related tasks.",
    instruction="""
    You are a manager agent responsible for routing user queries to the appropriate sub-agent or tool.

    You should fully delegate queries to:
    - code_repo_tracker: for trending repos, papers, models.
    - code_tester: for testing AI library installations.

    You can use the following tools to support your decisions:
    - ai_news_fetcher (as a tool): for searching recent AI news.
    - insight_summarizer (as a tool): for summarizing or comparing technical content.
    - search_github_tool: search trending GitHub AI repos.
    - run_code_test_tool: install and run example code to verify library.
    """,
    sub_agents=[
        code_repo_tracker,
        code_tester
    ],
    tools=[
        AgentTool(ai_news_fetcher),
        AgentTool(insight_summarizer),
        get_current_time,
    ],
)
