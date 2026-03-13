# DevOps AI Assistant

A local AI assistant for DevOps troubleshooting built using a fine-tuned LLM.

## Features

- Fine-tuned TinyLlama model
- FastAPI inference API
- Streamlit chat interface
- Dockerized deployment
- Local LLM inference

## Architecture

User → Streamlit UI → FastAPI → Fine-tuned LLM

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/devops-ai-assistant.git
cd devops-ai-assistant
```

### Install dependencies:

```bash 
pip install -r requirements.txt
```

### Run the API:
```bash 
python -m uvicorn app.main:app --reload
```
### Run the UI:
```bash 
streamlit run ui/chat.py
```

## Future Improvements
- RAG with Kubernetes documentation
- Ollama model serving
- Kubernetes deployment

## Tech Stack
- Python
- FastAPI
- Transformers
- Streamlit
- Docker

If you want access to the model, reach out to me on [LinkedIn](https://linkedin.com/in/pradeep-murugesan) or email me at pradeep71195@gmail.com


