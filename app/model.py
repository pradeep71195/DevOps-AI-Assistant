from transformers import pipeline

# Load model once at startup
pipe = pipeline(
    "text-generation",
    model="models/devops-ai-model",
    tokenizer="models/devops-ai-model",
    # device="cpu" or "gpu"  
)

def generate_answer(question: str):

    prompt = f"""
    ### Instruction:
    {question}

    ### Response:
    """

    result = pipe(
        prompt,
        max_new_tokens=300,
        temperature=0.7,
        top_p=0.9,
    )

    text = result[0]["generated_text"]

    # Clean response
    answer = text.split("### Response:")[-1].strip()

    return answer