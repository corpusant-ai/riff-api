"""
Print the timestamp of each lyric from the generation response.
"""
import riff_api

lyrics = """
Hello from outer space
Do you hear me?
Will I ever find my place
and set my spirit free?

[Chorus]
I'm a satellite
But I want to be by your side
""".strip()

response = riff_api.create(
    prompts=[
        riff_api.Prompt(text="chillstep pop"),
    ],
    lyrics=lyrics,
    save_to="6_timestamped_lyrics.wav",
)

# Print each word's start time
for word in response.timestamped_lyrics:
    print(f"{word.text:<12s} -> {word.start_s:6.1f}s")
