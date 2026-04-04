# Local Web-Augmented RAG Pipeline 🌐🧠

A highly reliable, native Python application that intercepts user queries, dynamically searches the live internet, and feeds the raw web data into a local Large Language Model (LLM) for synthesis. 

This project demonstrates a deterministic Retrieval-Augmented Generation (RAG) architecture, purposefully bypassing fragile ReAct (Reason and Act) agentic frameworks in favor of a bulletproof, hardcoded retrieval pipeline that prevents LLM parser failures.

## ✨ Key Features

* **Live Data Retrieval:** Utilizes the `duckduckgo-search` library to scrape real-time internet data without requiring paid API keys.
* **Deterministic Execution:** Guarantees tool execution via native Python logic, eliminating the risk of JSON-formatting hallucinations common in smaller local models.
* **Local Inference Synthesis:** Routes the retrieved web context to a locally hosted GGUF model (via LM Studio) for privacy-first reading and summarization.
* **Prompt Injection Defense:** Employs strict system prompts and zero-temperature configurations to force the model to answer *only* based on the provided search context.

## 🛠️ Tech Stack

* **Retrieval Engine:** `langchain_community`, `duckduckgo-search`
* **Inference Engine:** LM Studio (Localhost API), OpenAI Python Client
* **Language:** Python 3.10+
* **Architecture:** RAG (Retrieval-Augmented Generation)

## 🚀 Setup & Installation

**1. Install Dependencies**
Ensure you have Python installed, then grab the required routing and search libraries:

    pip install openai langchain-community duckduckgo-search

**2. Start the Local Brain**
Open LM Studio, load a general-instruct model (e.g., Llama-3-8B), and start the Local Inference Server on port 1234.

**3. Run the Pipeline**
Execute the main script. 

    python god_agent.py

## 💻 Architecture Flow

1. **Query Capture:** The user inputs a question (e.g., current events, stock prices).
2. **Pre-Inference Retrieval:** Python intercepts the query and natively executes a web search, downloading the top text results.
3. **Context Construction:** The raw web data is formatted into a strict instructional prompt alongside the user's original question.
4. **LLM Synthesis:** The local model reads the injected context and generates a human-readable, factual summary.