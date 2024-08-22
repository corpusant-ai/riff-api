"""
Print the timestamp of each lyric from the generation response.
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

save_audio(response, "7_timestamped_lyrics.wav")

# Print each word's start time
for word in response.timestamped_lyrics:
    print(f"{word.text:<12s} -> {word.start_s:6.1f}s")
