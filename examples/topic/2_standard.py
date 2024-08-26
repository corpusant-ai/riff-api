"""
Generate music from a single text description using /topic.
"""
import riff_api

response = riff_api.create_from_topic(
    topic="Explain the concept of time in French, piano chill",
    save_to="2_simple.wav",
)
