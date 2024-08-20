import os
import requests

from .datatypes import RiffRequest, RiffResponse


def generate_music(
    request: RiffRequest,
    api_key: str | None = None,
    endpoint: str = "https://api.riffusion.com/v1/riff",
) -> RiffResponse:
    """
    Generate music using the Riffusion API.
    """
    if api_key is None:
        api_key = os.environ.get("RIFFUSION_API_KEY")

    response = requests.post(
        url=endpoint,
        json=request.model_dump(),
        headers={
            "Authorization": f"Bearer {api_key}",
        },
    )

    response.raise_for_status()

    return RiffResponse(**response.json())
