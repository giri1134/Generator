from llama_cpp import Llama

# Load model ONCE
llm = Llama(
    model_path="models/model.gguf",
    n_ctx=2048,
    n_threads=8,  
    verbose=False
)

def generate_letter_body(letter_reason: str) -> str:
    """
    Generates ONLY the letter body.
    Must NOT include From/To/Subject.
    """

    prompt = f"""
You are a professional letter writer.

Rules:
- Write ONLY the body of the letter
- Do NOT include From address
- Do NOT include To address
- Do NOT include subject line
- Do NOT include date or signature
- Start directly with the greeting (e.g., Dear Sir/Madam)

Reason:
{letter_reason}

Letter body:
"""

    response = llm.create_completion(
        prompt=prompt,
        max_tokens=300,
        temperature=0.3,
        stop=["\n\nFrom:", "\n\nTo:", "\n\nSubject:"]
    )

    return response["choices"][0]["text"].strip()
