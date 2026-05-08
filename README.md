# Agents Playground

Agents Playground is a Streamlit chat application that demonstrates a LangChain ReAct agent with selectable LLM providers and web search tools.

The app lets you choose between OpenAI GPT-4, Google Gemini Pro, and Anthropic Claude 2.1, then routes user messages through a ReAct agent using either DuckDuckGo search or Tavily search. It also keeps chat history in Streamlit session state and includes an option to request Turkish responses.

![AI agent banner](img/ai_agent_banner.png)

## Features

- Streamlit chat interface
- LangChain ReAct agent built from the `hwchase17/react` hub prompt
- LLM selection:
  - GPT-4 via OpenAI
  - Gemini Pro via Google Generative AI
  - Claude 2.1 via Anthropic
- Search tool selection:
  - DuckDuckGo
  - Tavily
- Optional Turkish response mode
- Chat history reset button

## Project Structure

```text
.
├── customtools.py
├── img/
│   └── ai_agent_banner.png
├── react_chat.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- API keys for the providers you want to use

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
OPENAI_KEY=your_openai_api_key
GOOGLE_KEY=your_google_api_key
ANTHROPIC_KEY=your_anthropic_api_key
tavily_apikey=your_tavily_api_key
STABILITYAI_KEY=your_stability_ai_api_key
```

Only the keys for the models and tools you use are required at runtime. For example, Tavily search requires `tavily_apikey`, while DuckDuckGo search does not require an API key.

## Run

Start the Streamlit app:

```powershell
streamlit run react_chat.py
```

Then open the local URL printed by Streamlit, usually:

```text
http://localhost:8501
```

## Usage

1. Choose an LLM from the sidebar.
2. Choose a search engine.
3. Optionally keep Turkish response mode enabled.
4. Enter a message in the chat box.
5. Use **Reset the Chat History** to clear the current conversation.

## Notes

- `customtools.py` currently initializes OpenAI and loads several helper libraries, but its tools are not wired into `react_chat.py` yet.
- The sidebar includes image generation and web scraping selectors, but the current chat flow only uses the selected LLM and search engine.
- Do not commit your `.env` file or API keys to version control.
