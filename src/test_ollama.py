
from src.ollama_client import (
    check_ollama_connection,
    generate_response
)

if __name__ == "__main__":
    if check_ollama_connection():
        print("Ollama connection successful!")

        answer = generate_response(
            "Explain Retrieval Augmented Generation in two sentences."
        )

        print("\nModel response:")
        print(answer)
    else:
        print("Could not connect to Ollama.")
