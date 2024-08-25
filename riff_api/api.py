import base64
import os
import typing as T
import requests

from .datatypes import Prompt, RiffRequest, RiffResponse, TopicRequest


def generate(
    prompts: list[Prompt],
    lyrics: str | None = None,
    seed: int | None = None,
    audio_format: T.Literal["wav", "mp3", "m4a"] = "wav",
    moderate_inputs: bool = False,
    api_key: str | None = None,
    endpoint: str = "https://dev-backend.riffusion.com/v1/riff",
) -> RiffResponse:
    """
    Generate music using sound prompts and lyrics.
    """
    if api_key is None:
        api_key = os.environ.get("RIFFUSION_API_KEY")

    response = requests.post(
        url=endpoint,
        json=RiffRequest(
            prompts=prompts,
            lyrics=lyrics,
            seed=seed,
            audio_format=audio_format,
            moderate_inputs=moderate_inputs,
        ).model_dump(),
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


def generate_from_topic(
    topic: str,
    audio_format: str = "wav",
    api_key: str | None = None,
    endpoint: str = "https://dev-backend.riffusion.com/v1/topic",
) -> RiffResponse:
    """
    Generate music using a single text prompt encapsulating both
    the sound and the content of the output.
    """
    if api_key is None:
        api_key = os.environ.get("RIFFUSION_API_KEY")

    response = requests.post(
        url=endpoint,
        json=TopicRequest(
            topic=topic,
            audio_format=audio_format,
        ).model_dump(),
        headers={"Api-Key": api_key},
    )

    response.raise_for_status()

    return RiffResponse(**response.json())
