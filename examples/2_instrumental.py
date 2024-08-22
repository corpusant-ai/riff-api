"""
Pass no lyrics to create instrumental music.
"""
from riffusion_api import generate_music, save_audio, Prompt, RiffRequest

response = generate_music(
    RiffRequest(
        prompts=[
            Prompt(text="lo-fi cozy christmas jazz"),
        ],
    )
)

save_audio(response, "2_instrumental.wav")
