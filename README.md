# streamlit-expander-icon

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://expander-icon-demo.streamlit.app)

Streamlit's [`st.expander`](https://docs.streamlit.io/develop/api-reference/layout/st.expander) has a new `icon` parameter that allows you to set an icon or emoji for the expander. This can be a string representing an emoji, or a shortcode representing a Material icon.

| Parameter | Description |
| --- | --- |
| `icon` *(str, or None)* | An optional emoji or icon to display next to the button label. If `icon` is `None` (default), no icon is displayed. If `icon` is a string, the following options are valid: A single-character emoji. For example, you can set `icon="🚨"` or ``icon="🔥"``. Emoji short codes are not supported. An icon from the Material Symbols library (outlined style) in the format `":material/icon_name:"` where "icon_name" is the name of the icon in snake case. For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Outlined) font library. |

See the [PoC implementation](https://github.com/streamlit/streamlit/compare/develop...snehan/prototype/expander-icon).
