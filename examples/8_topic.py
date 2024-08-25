"""
Generate music from a single text description using /topic.
"""
import riff_api

response = riff_api.generate_from_topic("Country pop hit about my dog Erwin")

riff_api.save_audio(response, "8_topic.wav")
