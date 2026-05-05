from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
from langchain_core.messages.human import HumanMessage
from langchain_core.messages.system import SystemMessage

from app.config.setting import setting

def get_response_from_ai_agents(llm_id , query , allow_search ,system_prompt):

    llm = ChatGroq(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # Build messages with system prompt first, then user queries
    messages = []
    if system_prompt:
        messages.append(SystemMessage(content=system_prompt))
    
    # Convert string queries to HumanMessage objects
    messages.extend([HumanMessage(content=msg) if isinstance(msg, str) else msg for msg in query])
    state = {"messages" : messages}

    response = agent.invoke(state)

    messages = response.get("messages")

    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]

    return ai_messages[-1]





