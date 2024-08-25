import typing as T

from pydantic import BaseModel


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


class TimestampedWord(BaseModel):
    """
    A word from the lyrics with a start and end time
    """

    text: str
    start_s: float


class RiffResponse(BaseModel):
    """
    Output of the /riff endpoint
    """

    id: str
    """ UUID of the output"""

    audio_b64: str
    """ Base64 encoded bytes of the requested audio format """

    timestamped_lyrics: list[TimestampedWord]
    """ Timestamps for each word in the lyrics """


class TopicRequest(BaseModel):
    """
    Input to the /topic endpoint
    """

    topic: str
    """ Text description of the song to sing (lyrics and sound together) """

    audio_format: str = "wav"
    """ Returned audio format """
