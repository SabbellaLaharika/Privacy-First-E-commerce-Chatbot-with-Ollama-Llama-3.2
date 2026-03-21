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
```powershell
python -m venv venv
.\venv\Scripts\activate
```

## 4. Install Dependencies
```powershell
pip install requests datasets
```

## 5. Run the Chatbot or Data Prep
```powershell
# To run the chatbot evaluation:
python chatbot.py

# To run the data preparation sample:
python data_prep_sample.py
```
