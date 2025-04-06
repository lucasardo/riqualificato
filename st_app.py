####################################################################
### SETUP
####################################################################

import streamlit as st

st.set_page_config(page_title="Ama Barriera", page_icon="🔎") 

pages = {
    "Home": [
        st.Page("app_pages/home.py", title="Home"),
        st.Page("app_pages/barriera_da_vivere.py", title="Barriera da Vivere"),
        st.Page("app_pages/barriera_da_migliorare.py", title="Barriera da Migliorare"),
    ],
}

pg = st.navigation(pages)
pg.run()