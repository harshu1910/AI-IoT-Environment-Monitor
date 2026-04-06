import requests
import random
import time

while True:
    # Simulated sensor data
    temperature = random.randint(25, 45)
    humidity = random.randint(40, 80)

    prompt = f"Temperature is {temperature}°C and humidity is {humidity}%. What should I do?"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    print(f"\nTemp: {temperature}°C | Humidity: {humidity}%")
    print("AI:", response.json()['response'])
    print("-" * 40)

    time.sleep(5)