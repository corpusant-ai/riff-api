import streamlit as st

from riffusion.api import generate_music
from riffusion.datatypes import Prompt, RiffRequest


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

    # TODO

    st.write(response)


if __name__ == "__main__":
    main()
