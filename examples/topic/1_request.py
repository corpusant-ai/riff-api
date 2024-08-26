"""
Call the topic endpoint with `requests`, not using the Python client.
"""
import base64
import os
import requests

response = requests.post(
    "https://backend.riffusion.com/v1/topic",
    headers={
        "Content-Type": "application/json",
        "Api-Key": os.environ.get("RIFFUSION_API_KEY"),
    },
    json={
        "topic": "Indie pop banger about my dog Boris",
    },
).json()

with open("1_request.wav", "wb") as f:
    f.write(base64.b64decode(response["audio_b64"]))
