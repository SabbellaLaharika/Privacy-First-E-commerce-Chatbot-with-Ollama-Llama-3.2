import requests
import json
import os

# Constants
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return json.loads(response.text).get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return "Error: Could not get a response from the model."

def load_template(filename):
    with open(filename, 'r') as f:
        return f.read()

def main():
    # Load templates
    zero_shot_path = os.path.join("prompts", "zero_shot_template.txt")
    one_shot_path = os.path.join("prompts", "one_shot_template.txt")
    
    zero_shot_template = load_template(zero_shot_path)
    one_shot_template = load_template(one_shot_path)

    # 20 adapted e-commerce queries (Source: Ubuntu Dialogue Corpus v2.0)
    # See data_preparation.md for the full original-to-adapted mapping.
    queries = [
        "How do I track my recent order?",
        "My discount code isn't working at checkout.",
        "Can I change the shipping address after placing an order?",
        "What forms of payment do you accept?",
        "Do you offer international shipping?",
        "How do I cancel my order?",
        "I received a damaged item, what should I do?",
        "Are your products sustainably sourced?",
        "How do I reset my account password?",
        "Do you have a loyalty program for frequent shoppers?",
        "What is the expected delivery time for standard shipping?",
        "Can I exchange an item instead of returning it?",
        "Is there a physical store where I can try on clothes?",
        "Does the size 'Medium' run small for your t-shirts?",
        "How can I sign up for your newsletter?",
        "Are there any upcoming sales I should know about?",
        "Why was my credit card declined?",
        "Do you offer gift wrapping services?",
        "How do I use my store credit?",
        "What is the difference between your 'Classic' and 'Slim' fit jeans?"
    ]

    # Process and log results
    results_file = os.path.join("eval", "results.md")
    os.makedirs("eval", exist_ok=True)

    with open(results_file, "w") as f:
        f.write("# Evaluation Results\n\n")
        f.write("| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |\n")
        f.write("|---------|----------------|------------------|----------|-----------------|-----------------|--------------------|\n")

        for i, query in enumerate(queries, 1):
            print(f"Processing Query {i}/20: {query}")
            
            # Zero-shot
            zero_shot_prompt = zero_shot_template.format(query=query)
            zero_shot_response = query_ollama(zero_shot_prompt)
            f.write(f"| {i} | {query} | Zero-Shot | {zero_shot_response.replace('|', '/')} | - | - | - |\n")
            
            # One-shot
            one_shot_prompt = one_shot_template.format(query=query)
            one_shot_response = query_ollama(one_shot_prompt)
            f.write(f"| {i} | {query} | One-Shot | {one_shot_response.replace('|', '/')} | - | - | - |\n")

    print(f"Successfully processed {len(queries)} queries. Results saved to {results_file}.")

if __name__ == "__main__":
    main()
