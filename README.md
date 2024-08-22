# 🎸 Riffusion API

This repo contains minimal examples for creating music with the Riffusion API.

## Usage

Add your API key:

```bash
export RIFFUSION_API_KEY="<your-api-key>"
```

Run via Python:

```python
import base64
import os
import requests

response = requests.post(
    'https://backend.riffusion.com/v1/riff',
    headers={
        'Content-Type': 'application/json',
        'Api-Key': os.environ.get("RIFFUSION_API_KEY"),
    },
    json={
        'prompts': [
            { "text": "chillstep pop" },
        ],
        'lyrics': (
            "Hello from outer space\n"
            "Can you hear me?\n"
            "I'm a satellite\n"
            "And I want to be by your side"
        ),
    },
).json()

with open("output.wav", "wb") as f:
    f.write(base64.b64decode(response["audio_b64"]))
```

Run via Python with types:

```python
from riffusion.api import generate_music, Prompt, RiffRequest

lyrics = """
Hello from outer space
Can you hear me?
I'm a satellite
And I want to be by your side
""".strip()

response = generate_music(
    RiffRequest(
        prompts=[
            Prompt(text="chillstep pop"),
        ],
        lyrics=lyrics,
    )
)

import base64
with open("output.wav", "wb") as f:
    f.write(base64.b64decode(response.audio_b64))
```

Run via curl:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Api-Key: ${RIFFUSION_API_KEY}" \
  -d '{"prompts": [{"text": "chillstep pop"}], "lyrics": "Hello from outer space\nCan you hear me?"}' \
  https://backend.riffusion.com/v1/riff \
  | jq -r .audio_b64 | base64 -d > output.wav
```

## Examples

TODO

## Streamlit Demo

A simple Streamlit app is provided to demonstrate the API. This app allows
you to create a genre transition using two sound prompts with time ranges.

Test it at https://riffusion-api.streamlit.app/

To run locally:

```bash
python -m streamlit run demo_app.py
```

![Streamlit Demo](https://storage.googleapis.com/corpusant-public/riffusion_demo_app.png)
