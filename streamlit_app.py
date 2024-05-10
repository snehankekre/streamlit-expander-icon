import pandas as pd
import requests
import streamlit as st

st.set_page_config(
    page_title="Expander icons",
    page_icon=":fire:",
)

st.header("Icon support in st.expander", divider=True)

st.write(
    """
Streamlit's [`st.expander`](https://docs.streamlit.io/develop/api-reference/layout/st.expander) has a new `icon` parameter that allows you to set an icon or emoji for the expander. This can be a string representing an emoji, or a shortcode representing a Material icon.

| Parameter | Description |
| --- | --- |
| `icon` *(str, or None)* | An optional emoji or icon to display next to the button label. If `icon` is `None` (default), no icon is displayed. If `icon` is a string, the following options are valid: A single-character emoji. For example, you can set `icon="🚨"` or ``icon="🔥"``. Emoji short codes are not supported. An icon from the Material Symbols library (outlined style) in the format `":material/icon_name:"` where "icon_name" is the name of the icon in snake case. For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Outlined) font library. |
"""
)

st.write(
    """


"""
)

with st.sidebar.container(border=True):
    st.write(
        """
- 📚 [Add icon to st.expander](https://www.notion.so/snowflake-corp/Add-icon-to-st-expander-4b844d13357b430baf967265cfd2f5a6)
- Download the [wheel file](https://github.com/snehankekre/streamlit-expander-icon/raw/main/streamlit-1.34.0-py2.py3-none-any.whl)
- See the [PoC implementation](https://github.com/streamlit/streamlit/compare/develop...snehan/prototype/expander-icon).
"""
    )


@st.cache_resource
def get_emojis():
    resp = requests.get(
        "https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json"
    )
    json = resp.json()
    codes, emojis = zip(*json.items())
    df = pd.DataFrame(
        {
            "Emojis": emojis,
            "Shortcodes": [code for code in codes],
        }
    )
    df.set_index("Shortcodes", inplace=True)  # Set the shortcodes as the index
    return df


@st.cache_resource
def get_icons():
    resp = requests.get(
        "https://raw.githubusercontent.com/calasanmarko/material-icons-json/main/dist/icons.json"
    )
    json = resp.json()
    codes, _ = zip(*json.items())
    df = pd.DataFrame(
        {
            "Shortcodes": [code for code in codes],
        }
    )
    df = df[~df["Shortcodes"].str.contains("-")]
    return df


ALL_EMOJIS = get_emojis()
ALL_ICONS = get_icons()

st.sidebar.header("Select an emoji and icon")
st.sidebar.write("Your selections will be used in the expanders on the right.")
col1, col2 = st.sidebar.columns(2)
emoji = col1.selectbox(
    "Select an emoji",
    options=ALL_EMOJIS["Emojis"],
    format_func=lambda x: ALL_EMOJIS.loc[ALL_EMOJIS["Emojis"] == x].index[0],
    help="Find all Streamlit-supported emojis [here](https://share.streamlit.io/streamlit/emoji-shortcodes).",
)
icon = col2.selectbox(
    "Material icon",
    options=ALL_ICONS.iloc[::-1],
    help="Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Outlined) font library.",
)

st.subheader("With `icon` support")

with st.echo(code_location="below"):
    with st.expander("Click to expand", icon=emoji):
        st.dataframe(ALL_EMOJIS.reset_index(), use_container_width=True)

    with st.expander("Click to expand", icon=f":material/{icon}:"):
        st.dataframe(ALL_ICONS, use_container_width=True)

st.subheader("Using emojis/icon in labels (today)")

with st.echo(code_location="below"):
    with st.expander(f"{emoji} Click to expand"):
        st.dataframe(ALL_EMOJIS.reset_index(), use_container_width=True)

    with st.expander(f":material/{icon}: Click to expand"):
        st.dataframe(ALL_ICONS, use_container_width=True)
