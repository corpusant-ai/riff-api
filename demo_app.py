import base64
import time

import streamlit as st

from riffusion.api import generate_music, Prompt, RiffRequest

default_lyrics = """
[Verse]
All that is gold does not glitter
Not all those who wander are lost
The old that is strong does not wither
Deep roots are not reached by the frost

[Chorus]
From the ashes a fire shall be woken
A light from the shadows shall spring
""".strip()

prompts = [
    Prompt(
        text="operatic aria",
        start_s=0.0,
        end_s=20.0,
        strength=4.0,
    ),
    Prompt(
        text="tech house jazz",
        start_s=15.0,
        end_s=30.0,
        strength=3.0,
    ),
]


def main() -> None:
    """
    Basic streamlit demo for the Riffusion API that mixes two genres.

    Usage:
        python -m streamlit run demo_app.py
    """
    title = "Riffusion API Demo"
    icon = "🎸"

    st.set_page_config(page_title=title, page_icon=icon)

    st.write(f"### {title} {icon}")

    with st.form("form"):
        lyrics = st.text_area(
            "Lyrics",
            value=default_lyrics,
            height=250,
        )

        for prompt in prompts:
            with st.container():
                row = st.columns([3, 2, 2])
                prompt.text = row[0].text_input(
                    "Prompt",
                    value=prompt.text,
                )
                prompt.strength = row[1].number_input(
                    "Strength",
                    min_value=1.0,
                    max_value=12.0,
                    value=prompt.strength,
                )
                (prompt.start_s, prompt.end_s) = row[2].slider(
                    "Time Range",
                    min_value=0.0,
                    max_value=30.0,
                    value=(prompt.start_s, prompt.end_s),
                )

        st.form_submit_button("Generate", type="primary")

    request = RiffRequest(
        prompts=prompts,
        lyrics=lyrics,
        seed=None,
    )

    start_s = time.time()
    response = generate_music(request)
    duration_s = time.time() - start_s

    with st.expander("Request / Response"):
        st.write("#### Request")
        st.json(request.model_dump())

        st.write("#### Response")
        st.json({**response.model_dump(), "audio_b64": "<audio bytes>"})

    # Decode and display audio
    audio_bytes = base64.b64decode(response.audio_b64)
    st.audio(audio_bytes, format="audio/wav")

    st.write(f"⚡️ Generated in {duration_s:.2f} seconds")


if __name__ == "__main__":
    main()
