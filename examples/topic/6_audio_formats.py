"""
Change the audio format of the response.
"""
import riff_api

lyrics = """
Hello from outer space
Can you hear me?
I'm a satellite
And I want to be by your side
""".strip()

seed = 42

response_wav = riff_api.create(
    prompts=[
        riff_api.Prompt(text="chillstep pop"),
    ],
    lyrics=lyrics,
    audio_format="wav",  # also the default
    seed=seed,
)

riff_api.save_audio(response_wav, "6_audio_formats.wav")

response_m4a = riff_api.create(
    prompts=[
        riff_api.Prompt(text="chillstep pop"),
    ],
    lyrics=lyrics,
    audio_format="m4a",
    seed=seed,
)

riff_api.save_audio(response_m4a, "6_audio_formats.m4a")

response_mp3 = riff_api.create(
    prompts=[
        riff_api.Prompt(text="chillstep pop"),
    ],
    lyrics=lyrics,
    audio_format="mp3",
    seed=seed,
)

riff_api.save_audio(response_mp3, "6_audio_formats.mp3")
