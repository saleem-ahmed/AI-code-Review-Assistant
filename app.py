import streamlit as st

from config import *

from ui.home import show_home

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout=PAGE_LAYOUT,
)


def main():

    show_home()


if __name__ == "__main__":

    main()