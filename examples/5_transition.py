"""
Use two sound prompts with start/end times to control a transition.
"""
import riff_api

lyrics = """
[Verse]
All that is gold does not glitter
Not all those who wander are lost
The old that is strong does not wither
Deep roots are not reached by the frost

[Chorus]
From the ashes a fire shall be woken
A light from the shadows shall spring
""".strip()

prompts = [
    riff_api.Prompt(
        text="operatic aria",
        start_s=0.0,
        end_s=20.0,
        strength=4.0,
    ),
    riff_api.Prompt(
        text="tech house jazz",
        start_s=15.0,
        end_s=30.0,
        strength=3.0,
    ),
]

response = riff_api.generate(
    prompts=prompts,
    lyrics=lyrics,
)

riff_api.save_audio(response, "5_transition.wav")
