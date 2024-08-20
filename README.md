# Riffusion API


## Setup

Add your API key:

```bash
export RIFFUSION_API_KEY=<your-api-key>
```

Run via curl:

```bash
curl TODO
```

Run via Python:

```python
from riffusion.api import generate_music, Prompt, RiffRequest

response = generate_music(
    RiffRequest(
        prompts=[
            Prompt("country ballad"),
        ],
        lyrics="Sing me a song please, about a cowboy",
    )
)

import base64
with open("output.m4a", "wb") as f:
    f.write(base64.b64decode(response.audio))

```
