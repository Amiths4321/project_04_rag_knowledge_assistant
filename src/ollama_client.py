
import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434"
).rstrip("/")

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen2.5vl:latest"
)


def check_ollama_connection():
    """Check whether the Ollama server is reachable."""
    try:
        response = requests.get(
            f"{OLLAMA_URL}/api/tags",
            timeout=15
        )
        response.raise_for_status()
        return True

    except requests.RequestException as error:
        print(f"Ollama connection failed: {error}")
        return False


def generate_response(prompt):
    """Generate a response using the configured Ollama model."""
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()

        return response.json()["response"]

    except requests.RequestException as error:
        print(f"Ollama generation failed: {error}")
        return None
