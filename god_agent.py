from crewai import Agent, Task, Crew, LLM
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

print("🌐 Booting up Agentic Web Researcher...")

# 1. Connect to Local Brain (Temperature strictly at 0.0)
my_llm = LLM(
    model="openai/local-model", 
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    temperature=0.0 # ZERO creativity allowed for tool calling
)

web_search = DuckDuckGoSearchRun()

@tool("Live Internet Search")
def search_web(query: str) -> str:
    """Search the internet about a given topic and return relevant results."""
    return web_search.invoke(query)

# 2. The Bulletproof Prompt
researcher = Agent(
    role='Senior Intelligence Analyst',
    goal='Provide highly accurate answers by strictly using the Live Internet Search tool.',
    backstory='''You are an elite AI researcher. You MUST use the 'Live Internet Search' tool to answer the user.
    CRITICAL RULE: You must format your tool call EXACTLY like this, and you MUST include the closing bracket '}':
    
    Thought: I need to search the internet.
    Action: Live Internet Search
    Action Input: {"query": "your exact search phrase"}
    ''',
    tools=[search_web],
    llm=my_llm,
    verbose=True
)

print("-" * 50)
user_query = input("👨‍💻 You: What would you like me to research?\n> ")
print("-" * 50)

task = Task(
    description=f'Search the web to answer this exact query: "{user_query}".',
    expected_output='A concise, accurate summary of the web search results.',
    agent=researcher
)

crew = Crew(
    agents=[researcher],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()

print("\n================================================")
print("✅ FINAL REPORT:")
print(result)
print("================================================")