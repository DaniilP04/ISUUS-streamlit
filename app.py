import os.path

import streamlit as st
from streamlit_navigation_bar import st_navbar
from pages import Home,Project1,Project2,Project3
from PIL import Image

image = Image.open('img/tf2.png')

st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

logo_path = os.path.join(os.path.dirname(__file__),"img","Team_Fortress_2_style_logo.svg")
pages = ["Home","Project1","Project2","Project3"]
styles = {
    "nav": {
        "background-color": "rgb(205,53,53)",
        "display": "flex",
        "justify-content": "center",
    },
    "img": {
        "position": "absolute",
        "left": "-20px",
        "font-size": "15px",
        "top": "4px",
        "width": "100px",
        "height": "40px",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "display": "block",
        "color": "rgb(53,190,205)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255,229,204)",
        "font-weight": "normal",
        "padding": "14px",
    },
    "hover": {
        "background-color": "rgba(51,255,255)",
    },
}
options = {
    "show_menu": False,
    "show_sidebar": True,
}
page = st_navbar(pages, styles = styles, logo_path=logo_path,options=options)

if page == 'Home':
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()