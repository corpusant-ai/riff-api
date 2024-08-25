"""
Generate music from a single text description using /topic.
"""
import riff_api

# response = riff_api.generate_from_topic("Country pop hit about my dog Erwin")

# riff_api.save_audio(response, "8_topic.wav")

riff_api.generate_from_topic(
    topic="Indie pop banger about my dog Boris",
    save_to="8_topic.wav",
)