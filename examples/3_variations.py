"""
Hold a constant seed while modifying other parameters to create variations.
"""
import riff_api

lyrics = """
All that is gold does not glitter,
Not all those who wander are lost;
The old that is strong does not wither,
Deep roots are not reached by the frost.

From the ashes a fire shall be woken,
A light from the shadows shall spring;
Renewed shall be blade that was broken,
The crownless again shall be king.
""".strip()

# Use the seed to preserve the overall structure
seed = 90

variation_a = riff_api.generate(
    prompts=[
        riff_api.Prompt(text="country folk, male singer"),
    ],
    lyrics=lyrics,
    seed=seed,
)

riff_api.save_audio(variation_a, "3_variations_a.wav")

variation_b = riff_api.generate(
    prompts=[
        riff_api.Prompt(text="country folk, female singer"),
    ],
    lyrics=lyrics,
    seed=seed,
)

riff_api.save_audio(variation_b, "3_variations_b.wav")
