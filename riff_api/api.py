import base64
import os
import typing as T
import requests

from .datatypes import Prompt, RiffRequest, RiffResponse, TopicRequest

API_URL = os.environ.get(
    "RIFFUSION_BACKEND_URL",
    "https://backend.riffusion.com/v1",
)


def create_from_topic(
    topic: str,
    audio_format: str = "wav",
    api_key: str | None = None,
    save_to: str | None = None,
) -> RiffResponse:
    """
    Generate music using a single text prompt encapsulating both
    the sound and the content of the output.
    """
    if api_key is None:
        api_key = os.environ.get("RIFFUSION_API_KEY")

    request = TopicRequest(
        topic=topic,
        audio_format=audio_format,
    )

    response = requests.post(
        url=f"{API_URL}/topic",
        json=request.model_dump(),
        headers={"Api-Key": api_key},
    )

    response.raise_for_status()

    riff_response = RiffResponse(**response.json())

    if save_to is not None:
        assert (
            request.audio_format == save_to.split(".")[-1]
        ), "The save extension must match the audio format"
        save_audio(riff_response, save_to)

    return riff_response


def create(
    prompts: list[Prompt],
    lyrics: str | None = None,
    seed: int | None = None,
    audio_format: T.Literal["wav", "mp3", "m4a"] = "wav",
    moderate_inputs: bool = False,
    api_key: str | None = None,
    save_to: str | None = None,
) -> RiffResponse:
    """
    Generate music using sound prompts and lyrics.
    """
    return create_from_request(
        RiffRequest(
            prompts=prompts,
            lyrics=lyrics,
            seed=seed,
            audio_format=audio_format,
            moderate_inputs=moderate_inputs,
        ),
        api_key=api_key,
        save_to=save_to,
    )


def create_from_request(
    request: RiffRequest,
    api_key: str | None = None,
    save_to: str | None = None,
) -> RiffResponse:
    """
    Generate music given a RiffRequest object containing
    lyrics and sound prompts.
    """
    if api_key is None:
        api_key = os.environ.get("RIFFUSION_API_KEY")

    response = requests.post(
        url=f"{API_URL}/riff",
        json=request.model_dump(),
        headers={"Api-Key": api_key},
    )

    response.raise_for_status()

    riff_response = RiffResponse(**response.json())

    if save_to is not None:
        assert (
            request.audio_format == save_to.split(".")[-1]
        ), "The save extension must match the audio format"
        save_audio(riff_response, save_to)

    return riff_response


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
