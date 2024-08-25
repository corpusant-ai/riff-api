"""
Pass no lyrics to create instrumental music.
"""
import riff_api

response = riff_api.generate(
    prompts=[
        riff_api.Prompt(text="lo-fi cozy christmas jazz"),
    ],
)

riff_api.save_audio(response, "2_instrumental.wav")
