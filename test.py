import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": "Temperature is 35°C. Suggest actions.",
        "stream": False
    }
)

print(response.json()['response'])