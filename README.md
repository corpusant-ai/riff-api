# Riffusion API

![Banner](https://storage.googleapis.com/corpusant-public/banner.jpg)

This repo contains examples for crafting music using an API to Riffusion's foundational music models. The API is minimal and blazing fast, but also exposes powerful controllability features.

You can either use the typed Python client in this library or make requests directly. Please note that this API is in a private beta and subject to change.

Contact api@riffusion.com for inquiries and access.

## Get Started
Set your API key:

```bash
export RIFFUSION_API_KEY="<your-api-key>"
```

Install the Python client:
```bash
pip install riff-api
```

Make some music:

```python
import riff_api

riff_api.create_from_topic(
    "Indie pop banger about my dog Boris",
    save_to="output.wav",
)
```

Run multiple times to get different results.  
Here's a sample: [output.wav](https://storage.googleapis.com/corpusant-public/output.wav)

Have fun 💙

## `/topic` Endpoint

The `/topic` endpoint is the easiest way to create music. The input is a single natural language description of both the sound and lyrical content you desire.

Sample inputs:

 * "Indie pop banger about my dog Boris"
 * "Explain the concept of time in French, piano chill"
 * "Sing facts about Kansas history"

Run via Python client, this time saving the response:

```python
import riff_api

response = riff_api.create_from_topic(
    "Indie pop banger about my dog Boris",
    save_to="output.wav",
)
print(response.lyrics)
```

The audio, lyrics, and sound prompts are returned in the response object. The audio bytes are base64 encoded.

Alternatively, run directly via request:

```python
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

with open("output.wav", "wb") as f:
    f.write(base64.b64decode(response["audio_b64"]))
```

Or via curl:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Api-Key: ${RIFFUSION_API_KEY}" \
  -d '{"topic": "Indie pop banger about my dog Boris"}' \
  https://backend.riffusion.com/v1/topic \
  | jq -r .audio_b64 | base64 -d > output.wav
```

If you don't describe a musical style in your prompt, the API will choose randomly for you each time you call.

The schema of the entire API is defined in [datatypes.py](riff_api/datatypes.py).

### `/topic` Examples

 * [8_topic.py](examples/topic/8_topic.py) - Use a single natural language sentence to generate music with the topic endpoint.

 * [6_audio_formats.py](examples/riff/6_audio_formats.py) - Change the audio format of the response.

## `/riff` Endpoint

The `/riff` endpoint gives lower level control over the generation. You specify custom lyrics and a list of sound prompts with individual strengths and time ranges.

Run via Python client:

```python
import riff_api

lyrics = """
Hello from outer space
Can you hear me?
I'm a satellite
And I want to be by your side
""".strip()

response = riff_api.create(
    prompts=[
        Prompt(text="chillstep pop"),
    ],
    lyrics=lyrics,
    save_to="output.wav",
)
```

Run via request:

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

### `/riff` Examples

The [examples/riff](examples/riff) directory explains use cases of the API.

 * [1_simple.py](examples/riff/1_simple.py) - Use lyrics and a sound prompt to create music.

 * [2_instrumental.py](examples/riff/2_instrumental.py) - Pass no lyrics to create instrumental music.

 * [3_variations.py](examples/riff/3_variations.py) - Hold a constant seed while modifying other parameters to create variations.

 * [4_multiple_prompts.py](examples/riff/4_multiple_prompts.py) - Use two sound prompts with different strengths to fine tune the output.

 * [5_transition.py](examples/riff/5_transition.py) - Use two sound prompts with start/end times to create a transition.

 * [6_timestamped_lyrics.py](examples/riff/6_timestamped_lyrics.py) - Print the timestamp of each lyric from the generation response.


## Streamlit Demo

[demo_app.py](demo_app.py) is a basic web app that
demonstrates using the api to create musical transitions using two sound prompts
with time ranges.

Try it: [https://riffusion-api-demo.streamlit.app/](https://riffusion-api-demo.streamlit.app/)

Or run locally:

```bash
pip install streamlit
python -m streamlit run demo_app.py
```

<img src="https://storage.googleapis.com/corpusant-public/riffusion_demo_app.png" width="500px" />
