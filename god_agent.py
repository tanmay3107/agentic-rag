from langchain_community.tools import DuckDuckGoSearchRun
from openai import OpenAI

print("🌐 Booting up Native Web Agent...")

# 1. Connect to Local Brain
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# 2. Setup Web Search
web_search = DuckDuckGoSearchRun()

print("-" * 50)
user_query = input("👨‍💻 You: What would you like me to research?\n> ")
print("-" * 50)

# 3. Python runs the search FIRST (Bypassing the AI's need to write JSON)
print("🔍 Browsing the live internet...")
try:
    search_results = web_search.invoke(user_query)
except Exception as e:
    search_results = f"Search failed: {e}"

# 4. We feed the raw web data directly to the LLM to summarize
print("🧠 Analyzing results...")
prompt = f"""
You are an elite researcher. Answer the user's question based ONLY on the following live web search results. Do not guess.

User's Question: {user_query}

Live Web Search Results:
{search_results}
"""

response = client.chat.completions.create(
    model="local-model",
    messages=[
        {"role": "system", "content": "You are a factual, concise AI assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3
)

print("\n================================================")
print("✅ FINAL REPORT:")
print(response.choices[0].message.content)
print("================================================")