import base64
import time

import requests
import streamlit as st

import riff_api

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
    riff_api.Prompt(
        text="operatic aria",
        start_s=0.0,
        end_s=20.0,
        strength=4.0,
    ),
    riff_api.Prompt(
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
    icon = "💫"

    st.set_page_config(page_title=title, page_icon=icon)

    st.write(f"### {icon} {title}")

    tabs = st.tabs(
        [
            "**Topic Endpoint**",
            "**Riff Endpoint**",
            "**Setup**",
        ]
    )

    with tabs[0]:
        topic_tab()

    with tabs[1]:
        riff_tab()

    with tabs[2]:
        with st.container(border=True):
            setup_tab()

    if "response" not in st.session_state:
        return

    response: riff_api.RiffResponse = st.session_state.response
    duration_s = st.session_state.duration_s

    st.write("#### Latest Creation")

    # Decode and display audio
    audio_bytes = base64.b64decode(response.audio_b64)
    st.audio(audio_bytes, format="audio/wav")
    st.caption(f"⚡️ Generated in {duration_s:.2f} seconds")

    prompt_str = ", ".join([prompt.text for prompt in response.prompts])
    st.write(f"##### {prompt_str}")

    # Display lyrics
    if response.lyrics:
        st.text(response.lyrics)


def topic_tab() -> None:
    with st.form("topic_form", border=True):
        topic = st.text_input(
            "Topic",
            value="Indie pop banger about my dog Boris",
        )
        submitted = st.form_submit_button("Generate", type="primary")

    if not submitted:
        return

    call_api(
        riff_api.create_from_topic,
        topic,
    )


def riff_tab() -> None:
    with st.form("riff_form"):
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
                    min_value=-3.0,
                    max_value=12.0,
                    value=prompt.strength,
                )
                (prompt.start_s, prompt.end_s) = row[2].slider(
                    "Time Range",
                    min_value=0.0,
                    max_value=30.0,
                    value=(prompt.start_s, prompt.end_s),
                )

        submitted = st.form_submit_button("Generate", type="primary")

    if not submitted:
        return

    request = riff_api.RiffRequest(
        prompts=prompts,
        lyrics=lyrics,
        seed=None,
    )

    call_api(
        riff_api.create_from_request,
        request,
    )


def call_api(func, *args, **kwargs) -> None:
    if "api_key" not in st.session_state:
        st.error("Please enter an API key in the Setup tab")
        return

    api_key = st.session_state.api_key
    if not api_key:
        st.info(
            "Enter your API key in the Setup tab. "
            "Contact api@riffusion.com for access."
        )
        return

    start_s = time.time()

    try:
        response = func(
            *args,
            **kwargs,
            api_key=api_key,
        )
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            st.error("[401] Unauthorized API Key")
        else:
            st.error(f"HTTP Error: {e}")
        return
    except Exception as e:
        st.error(f"Error: {e}")
        return

    st.session_state.duration_s = time.time() - start_s
    st.session_state.response = response


def setup_tab() -> None:
    st.write(
        "This is a web demo for creating music with the Riffusion API.  \n"
        "Enter your API key to get started, or contact api@riffusion.com for access."
    )

    api_key = st.text_input("API Key", type="password")
    st.session_state.api_key = api_key

    st.write("See https://github.com/corpusant-ai/riff-api for more information.")


if __name__ == "__main__":
    main()
