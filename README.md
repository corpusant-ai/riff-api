# 🎸 Riffusion API

This repo contains minimal examples for creating music with the Riffusion API.

> [!NOTE]  
> This API is in a private beta and subject to change. Contact api@riffusion.com for questions.

## Usage

Add your API key:

```bash
export RIFFUSION_API_KEY="<your-api-key>"
```

Run via Python (`pip install requests`):

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

Run via Python with types (`pip install .`):

```python
from riffusion_api import generate_music, Prompt, RiffRequest

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

The file [datatypes.py](riffusion_api/datatypes.py) shows the schema of the API.

## Examples

The `examples` directory explains use cases of the API. To run, first `pip install .` then execute with Python 3.

 * [1_simple.py](examples/1_simple.py) - Use lyrics and a sound prompt to create music.

 * [2_instrumental.py](examples/2_instrumental.py) - Pass no lyrics to create instrumental music.

 * [3_variations.py](examples/3_variations.py) - Hold a constant seed while modifying other parameters to create variations.

 * [4_multiple_prompts.py](examples/4_multiple_prompts.py) - Use two sound prompts with different strengths to fine tune the output.

 * [5_transition.py](examples/5_transition.py) - Use two sound prompts with start/end times to create a transition.

 * [6_audio_formats.py](examples/6_audio_formats.py) - Change the audio format of the response.

 * [7_timestamped_lyrics.py](examples/7_timestamped_lyrics.py) - Print the timestamp of each lyric from the generation response.

## Streamlit Demo

[demo_app.py](demo_app.py) is an interactive web app (built with Streamlit) that
demonstrates using the api to create musical transitions using two sound prompts
with time ranges.

Try it at: [https://riffusion-api-demo.streamlit.app/](https://riffusion-api-demo.streamlit.app/)

Run locally:

```bash
python -m streamlit run demo_app.py
```

<img src="https://storage.googleapis.com/corpusant-public/riffusion_demo_app.png" width="500px" />
