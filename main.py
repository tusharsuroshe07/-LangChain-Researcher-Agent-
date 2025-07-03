from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from tools.search_tools import wiki_search, web_search
from tools.pdf_tools import load_and_query_pdf

llm = ChatOpenAI(temperature=0)

memory = ConversationBufferMemory(memory_key="chat_history")

tools = [
    Tool(name="Wikipedia Search", func=wiki_search, description="Searches Wikipedia."),
    Tool(name="Web Search", func=web_search, description="Searches the web for current information."),
    Tool(name="PDF Research", func=load_and_query_pdf, description="Extracts and answers from local PDFs.")
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory
)

while True:
    query = input("\nAsk a research question (or type 'exit'): ")
    if query.lower() == 'exit':
        break
    result = agent.run(query)
    print("\n📄 Result:", result)
