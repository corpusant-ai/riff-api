"""
Use two sound prompts with start/end times to control a transition.
"""
from riffusion_api import generate_music, save_audio, Prompt, RiffRequest

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
    Prompt(
        text="operatic aria",
        start_s=0.0,
        end_s=20.0,
        strength=4.0,
    ),
    Prompt(
        text="tech house jazz",
        start_s=15.0,
        end_s=30.0,
        strength=3.0,
    ),
]

response = generate_music(
    RiffRequest(
        prompts=prompts,
        lyrics=lyrics,
    )
)

save_audio(response, "5_transition.wav")
