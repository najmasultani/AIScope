# 🤖 AISCOPE: Multi-Agent AI System using Google's ADK

AISCOPE is a modular multi-agent system built with [Google's Agent Development Kit (ADK)](https://google.github.io/adk-docs/). It demonstrates how intelligent agents can collaborate to handle diverse AI-related tasks such as repository tracking, code testing, news summarization, and content analysis — all managed by a central controller agent.

---

## 📦 Features

- 🧠 **Manager Agent**: Delegates tasks intelligently across the system
- 📈 **Code Repository Tracker**: Monitors trending AI projects on GitHub
- 🧪 **Code Tester**: Installs and tests Python libraries with example code
- 📰 **AI News Fetcher**: Retrieves and summarizes current AI news
- 📚 **Insight Summarizer**: Analyzes and compares technical content (papers, changelogs, READMEs)

---

## 🗂️ Project Structure

```
AISCOPE/
├── agent.py                   # Root manager agent
├── .env                       # API key configuration
├── sub_agents/
│   ├── code_repo_tracker/
│   │   └── agent.py
│   ├── code_tester/
│   │   └── agent.py
│   ├── ai_news_fetcher/
│   │   └── agent.py
│   └── insight_summarizer/
│       └── agent.py
```

Each sub-agent is self-contained and exposes a single `Agent` object. The manager imports and coordinates them via ADK’s `Agent` and `AgentTool` patterns.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/aiscope.git
cd aiscope
```

### 2. Set Up Your Environment

```bash
python -m venv .venv
source .venv/bin/activate        # or .venv\Scripts\activate on Windows
pip install -r requirements.txt  # if you have one
```

### 3. Configure API Key

Create a `.env` file in the project root and add:

```env
GOOGLE_API_KEY=your-api-key-here
```

---

## 💡 How It Works

The manager agent acts as a central router. Depending on the query:

- It can **delegate** fully to sub-agents (e.g., code tester)
- Or use **agent tools** to retrieve data, summarize, and respond with integrated results

This hybrid design allows flexibility while complying with ADK’s tool-use restrictions.

---

## 🧪 Example Prompts

Try these in the ADK web UI:

- "What are the top trending AI repos this week?"
- "Install `transformers` and run a sample inference."
- "Summarize the differences between Llama 3 and GPT-4."
- "What’s new in AI news today?"

---

## ▶️ Run the App

```bash
adk web
```

Then open [http://localhost:8000](http://localhost:8000) and select the **manager** agent to begin chatting.

---

## 🛠️ Notes

- Run all commands from the root folder (`AISCOPE/`)
- Only one tool type (built-in **or** custom) is allowed per sub-agent
- Built-in tools can still be used via `AgentTool` at the manager level

---

## 📄 License

This project is licensed under the MIT License.

---

## 📚 Resources

- [ADK Docs (Google)](https://google.github.io/adk-docs/)
- [AgentTool Usage Guide](https://google.github.io/adk-docs/tools/function-tools/#3-agent-as-a-tool)
- [agent-development-kit-crash-course](https://github.com/bhancockio/agent-development-kit-crash-course/tree/main)
