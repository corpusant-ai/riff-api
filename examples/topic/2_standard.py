"""
Call the topic endpoint with the Python client.
"""
import riff_api

response = riff_api.create_from_topic(
    "Explain the concept of time in French, piano chill",
    save_to="2_standard.wav",
)
