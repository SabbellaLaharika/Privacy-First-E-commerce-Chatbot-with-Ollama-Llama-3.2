# Setup Instructions

To run the Offline Customer Support Chatbot, follow these steps:

## 1. Install Ollama
Download and install Ollama from [ollama.com](https://ollama.com/).

## 2. Pull Llama 3.2 Model
Open your terminal and run:
```bash
ollama pull llama3.2:3b
```

## 3. Python Environment Setup
It is recommended to use a virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

## 4. Install Dependencies
```bash
pip install requests
```

## 5. Run the Chatbot
Ensure Ollama is running, then execute:
```bash
python chatbot.py
```
This will generate `eval/results.md` with responses from the model.
