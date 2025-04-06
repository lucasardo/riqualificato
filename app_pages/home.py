import streamlit as st

# Add a title and description at the top of the page
st.title("RiqualificaTO - Barriera edition")
st.write("La tua app per condividere idee e progetti su come migliorare il tuo quartiere 🌍")

# Add two buttons in the middle of the page with a red background and a link to two web pages
st.markdown(
    """
    <style>
    .red-button {
        background-color: red;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
col1, col2 = st.columns(2)
with col1:
    st.image("images/vivere.jpeg", use_container_width=True)
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px; margin-bottom: 50px;">
            <a href="https://riqualificato-green-digital-futures.streamlit.app/barriera_da_vivere" class="red-button" style="display: inline-block; padding: 20px 20px; text-decoration: none; color: white;">Barriera da Vivere</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
with col2:    
    st.image("images/migliorare.jpeg", use_container_width=True)
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px; margin-bottom: 50px;">
            <a href="https://riqualificato-green-digital-futures.streamlit.app/barriera_da_migliorare" class="red-button" style="display: inline-block; padding: 20px 20px; text-decoration: none; color: white;">Barriera da Migliorare</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
