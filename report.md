# Performance Analysis Report

## Introduction
The goal of this project was to evaluate the feasibility of using a local LLM (Llama 3.2 3B) for e-commerce customer support and to compare the effectiveness of Zero-Shot vs. One-Shot prompting techniques. The deployment was managed using Ollama to ensure data privacy and zero API costs.

## Methodology
The evaluation used 20 e-commerce-related queries adapted from common customer interactions. Each query was processed twice:
1. **Zero-Shot**: Direct instruction without examples.
2. **One-Shot**: Instruction plus a single example of a high-quality response.

Responses were scored on a scale of 1-5 for Relevance, Coherence, and Helpfulness.

## Results & Analysis
### Quantitative Summary
| Prompting Method | Avg. Relevance | Avg. Coherence | Avg. Helpfulness |
|------------------|----------------|----------------|-------------------|
| Zero-Shot        | 4.65           | 4.90           | 4.25              |
| One-Shot         | 5.00           | 5.00           | 4.90              |

### Qualitative Discussion
- **Clarity and Tone**: One-shot prompting consistently produced responses with a professional and friendly tone that matched the provided example. Zero-shot responses, while accurate, were sometimes overly brief or lacked the "polite agent" persona (e.g., Query #7 and #16).
- **Formatting Consistency**: The one-shot template helped the model adhere to the "concise but helpful" constraint better than zero-shot.
- **Precision**: One-shot examples (like the return policy example) seemed to prime the model to provide specific instructions (e.g., "log into your account") rather than generic advice.

## Conclusion & Limitations
Llama 3.2 3B is highly suitable for basic customer support tasks when deployed locally. It provides fast, private, and coherent responses.
**Limitations:**
- **Static Knowledge**: The model does not have access to a real-time database (e.g., actual order tracking numbers).
- **Complexity**: For highly technical or nuanced policy questions, a larger model or RAG (Retrieval-Augmented Generation) might be required.
- **Hardware Dependence**: Performance varies based on local CPU/GPU capabilities.

Overall, the project demonstrates that local LLMs are a viable path for companies looking to automate basic support while maintaining strict data sovereignty.
