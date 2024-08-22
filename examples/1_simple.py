"""
Use lyrics and a sound prompt to create music.
"""
from riffusion_api import generate_music, save_audio, Prompt, RiffRequest

lyrics = """
Hello from outer space
Can you hear me?
I'm a satellite
And I want to be by your side
""".strip()

response = generate_music(
    RiffRequest(
        prompts=[
            Prompt(text="chillstep pop"),
        ],
        lyrics=lyrics,
    )
)

save_audio(response, "1_simple.wav")
