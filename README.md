# -LangChain-Researcher-Agent-
The LangChain Researcher Agent is an AI-driven tool designed to autonomously gather, synthesize, and analyze information from various sources to answer complex research questions. It leverages language models and tools like web search, document loaders, and vector stores to provide accurate, contextual responses.

# Use Zip File For All Code 

# 🧠 LangChain Researcher Agent 

This is an advanced Researcher Agent built with LangChain.

## ✅ Features
- 🔎 Wikipedia search tool
- 🌐 Web search (mocked; add SerpAPI if needed)
- 📄 PDF document reading (via `docs/sample.pdf`)
- 🧠 Conversational memory
- 🧰 Extendable tools

## 🚀 How to Use

### 1. Install requirements
```bash (Terminal )
pip install -r requirements.txt
```

### 2. Set your OpenAI API Key
```bash  (Terminal )
export OPENAI_API_KEY=your_key_here  # or set on Windows
```

### 3. Run the Agent
```bash  (Terminal )
python main.py
```

### 4. Ask questions like:
- What is reinforcement learning?
- Summarize the sample PDF
- What is in the news about AI?

## 🔄 PDF Support
Replace `docs/sample.pdf` with your own paper/article for instant Q&A.

