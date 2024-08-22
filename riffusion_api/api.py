import base64
import os
import requests

from .datatypes import RiffRequest, RiffResponse


def generate_music(
    request: RiffRequest,
    api_key: str | None = None,
    endpoint: str = "https://dev-backend.riffusion.com/v1/riff",
) -> RiffResponse:
    """
    Generate music using the Riffusion API.
    """
    if api_key is None:
        api_key = os.environ.get("RIFFUSION_API_KEY")

    response = requests.post(
        url=endpoint,
        json=request.model_dump(),
        headers={"Api-Key": api_key},
    )

    response.raise_for_status()

    return RiffResponse(**response.json())


def save_audio(
    response: RiffResponse,
    filename: str,
) -> None:
    """
    Save the audio from a Riffusion response to a file.
    """
    audio_bytes = base64.b64decode(response.audio_b64)
    with open(filename, "wb") as f:
        f.write(audio_bytes)
