from datasets import load_dataset

def main():
    print("Loading Ubuntu Dialogue Corpus (v2.0)...")
    try:
        # Note: This is a large dataset. This script demonstrates the sourcing methodology.
        dataset = load_dataset("rguo12/ubuntu_dialogue_corpus", "v2.0")
        train_data = dataset['train']
        print(f"Successfully loaded {len(train_data)} dialogues.")
        
        # Methodology:
        # 1. Browse technical support queries in the corpus.
        # 2. Extract 20 varied technical questions.
        # 3. Manually adapt them into plausible e-commerce scenarios.
        # These 20 adapted queries are now hardcoded in 'chatbot.py'.
        
    except Exception as e:
        print(f"Error loading dataset: {e}")
        print("Note: You may need to install 'datasets' using 'pip install datasets'.")

if __name__ == "__main__":
    main()
