import base64

import streamlit as st

from riffusion.api import generate_music, Prompt, RiffRequest


def main() -> None:
    """
    Foo
    """
    st.write("# 🎸 Riffusion API Demo")

    request = RiffRequest(
        prompts=[
            Prompt(text="country folk"),
        ],
        lyrics="I'm feeling happy and sad",
    )

    response = generate_music(request)

    audio_bytes = base64.b64decode(response.audio_b64)

    st.audio(audio_bytes, format="audio/m4a")

    # TODO show timestamped lyrics

if __name__ == "__main__":
    main()
