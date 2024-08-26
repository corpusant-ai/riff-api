"""
Use two sound prompts with different strengths to fine tune the output.
"""
import riff_api

lyrics = """
[Chorus]
Light the hearth, sing out clear,
Christmas moments, hold them dear,
Gather 'round, the time is here,
For love and laughter, far and near.
""".strip()

response = riff_api.create(
    prompts=[
        riff_api.Prompt(
            text="punk rock",
            strength=4.0,
        ),
        riff_api.Prompt(
            text="tribal chanting and drums",
            strength=6.0,
        ),
    ],
    lyrics=lyrics,
    seed=800,
)

riff_api.save_audio(response, "4_multiple_prompts.wav")
