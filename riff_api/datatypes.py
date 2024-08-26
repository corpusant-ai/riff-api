import typing as T

from pydantic import BaseModel


class TopicRequest(BaseModel):
    """
    Input to the /topic endpoint
    """

    topic: str
    """ Text description of the song to sing (lyrics and sound together) """

    audio_format: str = "wav"
    """ Returned audio format """


class TimestampedWord(BaseModel):
    """
    A word with a timestamp
    """

    text: str
    start_s: float


class Prompt(BaseModel):
    """
    A sound prompt to use for music generation
    """

    text: str
    """ Description of the sound """

    strength: float = 4.0
    """ Power of this prompt between 1 (low) and 12 (max) """

    start_s: float = 0.0
    """ Start time where the prompt takes effect """

    end_s: float = 30.0
    """ End time where the prompt takes effect"""


class RiffRequest(BaseModel):
    """
    Input to the /riff endpoint
    """

    prompts: list[Prompt]
    """ A list of sound prompts """

    lyrics: str | None = None
    """ Lyrics to sing (optional) """

    seed: int | None = None
    """ Random seed for reproducible results (optional) """

    audio_format: T.Literal["wav", "m4a", "mp3"] = "wav"
    """ Returned audio format """

    moderate_inputs: bool = True
    """ If True, runs moderation checks on the prompts and lyrics """


class RiffResponse(BaseModel):
    """
    Output of the /riff and /topic endpoints
    """

    id: str
    """ UUID of the output"""

    audio_b64: str
    """ Base64 encoded bytes of the requested audio format """

    lyrics: str | None
    """ Lyrics of the song, if present """

    timestamped_lyrics: list[TimestampedWord] | None
    """ Timestamps for each word in the lyrics """

    prompts: list[Prompt]
    """ List of sound prompts used to create the sample """
