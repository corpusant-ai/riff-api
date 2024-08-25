"""
Use lyrics and a sound prompt to create music.
"""
import riff_api

lyrics = """
Hello from outer space
Can you hear me?
I'm a satellite
And I want to be by your side
""".strip()

response = riff_api.generate(
    prompts=[
        riff_api.Prompt(text="chillstep pop"),
    ],
    lyrics=lyrics,
)

riff_api.save_audio(response, "1_simple.wav")
