from crewai import Agent, Task, Crew, LLM
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

print("🌐 Booting up Agentic Web Researcher...")

# 1. Connect to Local Brain (LM Studio)
# Make sure LM Studio is running on port 1234!
my_llm = LLM(
    model="openai/local-model", 
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    temperature=0.2
)

# 2. Define the Tool (The Agent's Toolbelt)
web_search = DuckDuckGoSearchRun()

@tool("Live Internet Search")
def search_web(query: str) -> str:
    """Useful to search the internet about a given topic and return relevant results."""
    return web_search.invoke(query)

# 3. Create the Autonomous Agent
researcher = Agent(
    role='Senior Intelligence Analyst',
    goal='Provide highly accurate answers by strictly using the internet search tool.',
    backstory='''You are an elite researcher. You do not know current events, so you MUST use your search tool. 
    CRITICAL RULE: To use your tool, you must format your response EXACTLY like this:
    Thought: I need to search the internet for this.
    Action: Live Internet Search
    Action Input: {"query": "your search phrase here"}''',
    tools=[search_web],
    llm=my_llm,
    verbose=True
)

# 4. Get User Input
print("-" * 50)
user_query = input("👨‍💻 You: What would you like me to research?\n> ")
print("-" * 50)

# 5. Define the Task
task = Task(
    description=f'Research and answer this query: "{user_query}". If needed, use your search tool.',
    expected_output='A concise, accurate summary of the findings.',
    agent=researcher
)

# 6. Run the Swarm
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