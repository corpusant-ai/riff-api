# Riffusion API

![Banner](https://storage.googleapis.com/corpusant-public/banner.jpg)

This repo contains code for crafting music using Riffusion's foundational music models via API. You can either use the typed Python client in this library or make requests directly.

Please note that this API is in a private beta and subject to change. Contact api@riffusion.com for inquiries and access.

## Getting Started
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

This will generate lyrics and music for a 30s song. Run multiple times to create variations.

Sample: [output.wav](https://storage.googleapis.com/corpusant-public/output.wav)

Have fun 💙

## `/topic` Endpoint

This endpoint creates a song from a single natural language description the desired lyrical content and/or musical style. It's the simplest way to create.

The API will generate lyrics based on your topic, as well as pick specific sound prompts. If you don't describe a musical style in your prompt, the API will choose randomly for you each time you call.

Get creative with your topics! Here are a few ideas:

 * "Rap fun facts about Alaska's history"
 * "Explain the concept of time in French"
 * "My nephew Remi is a superhero with laser eyes. Make him a theme song with a rock orchestra"

Run via Python client, saving the audio (decoded from base64) and printing the generated lyrics:

```python
import riff_api

response = riff_api.create_from_topic(
    "Rap fun facts about Alaskan history",
    save_to="output.wav",
)
print(response.lyrics)
```

Alternatively, execute a request directly instead of using the Python client:

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
        "topic": "Rap fun facts about Alaskan history",
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
  -d '{"topic": "Rap fun facts about Alaskan history"}' \
  https://backend.riffusion.com/v1/topic \
  | jq -r .audio_b64 | base64 -d > output.wav
```

### Examples

Check out [examples/topic](examples/topic) for runnable scripts that demonstrate this endpoint.

 * [1_request.py](examples/topic/1_request.py) - Call the topic endpoint with `requests`, not using the Python client.

 * [2_standard.py](examples/topic/2_standard.py) - Call the topic endpoint with the Python client.

The full schema is in [datatypes.py](riff_api/datatypes.py).

## `/riff` Endpoint

This endpoint provides a more powerful capability for music lovers to craft the exact sound they want. You can specify custom lyrics and multiple sound prompts with individually controllable strengths and time ranges.

Here's a call that creates a 10 second orchestral intro in a chillstep pop song with custom lyrics:

```python
import riff_api

lyrics = """
Hello from outer space
Can you hear me?
I'm a satellite
And I want to be by your side
""".strip()

riff_api.create(
    prompts=[
        riff_api.Prompt(
            text="chillstep pop",
            strength=4.0,
        ),
        riff_api.Prompt(
            text="orchestral cellos",
            strength=3.0,
            start_s=0.0,
            end_s=10.0,
        ),
    ],
    lyrics=lyrics,
    save_to="output.wav",
)
```

### Examples

Check out [examples/riff](examples/riff) for runnable scripts that demonstrate this endpoint.

 * [1_simple.py](examples/riff/1_simple.py) - Use lyrics and a sound prompt to create music.

 * [2_instrumental.py](examples/riff/2_instrumental.py) - Pass no lyrics to create instrumental music.

 * [3_variations.py](examples/riff/3_variations.py) - Hold a constant seed while modifying other parameters to create variations.

 * [4_multiple_prompts.py](examples/riff/4_multiple_prompts.py) - Use two sound prompts with different strengths to fine tune the output.

 * [5_transition.py](examples/riff/5_transition.py) - Use two sound prompts with start/end times to create a transition.

 * [6_timestamped_lyrics.py](examples/riff/6_timestamped_lyrics.py) - Print the timestamp of each lyric from the generation response.

 * [7_audio_formats.py](examples/riff/7_audio_formats.py) - Change the audio format of the response.

The full schema is in [datatypes.py](riff_api/datatypes.py).

## Streamlit Demo

[demo_app.py](demo_app.py) is a basic web app built with Streamlit that
demonstrates using the api.

Try it: [https://riff-api.streamlit.app](https://riff-api.streamlit.app)

Or run locally:

```bash
pip install streamlit
python -m streamlit run demo_app.py
```

<img src="https://storage.googleapis.com/corpusant-public/riffusion_demo_app.png" width="500px" />
