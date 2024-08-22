"""
Use two sound prompts with different strengths to fine tune the output.
"""
from riffusion_api import generate_music, save_audio, Prompt, RiffRequest

lyrics = """
[Chorus]
Light the hearth, sing out clear,
Christmas moments, hold them dear,
Gather 'round, the time is here,
For love and laughter, far and near.
""".strip()

response = generate_music(
    RiffRequest(
        prompts=[
            Prompt(
                text="punk rock",
                strength=4.0,
            ),
            Prompt(
                text="tribal chanting and drums",
                strength=6.0,
            ),
        ],
        lyrics=lyrics,
        seed=800,
    )
)

save_audio(response, "4_multiple_prompts.wav")
