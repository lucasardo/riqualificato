import streamlit as st
import pandas as pd
import pydeck as pdk

# Placeholder dataset for events
events = pd.DataFrame({
    "Categoria": ["Traffico", "Aree abbandonate"],
    "Nome Evento": ["Piazza Baldissera", "Fabbrica ex-Gondrand"],
    "Indirizzo": ["Piazza Generale Baldissera, Torino", "Via Fossata, Torino"],
    "Latitude": [45.0918, 45.0934],
    "Longitude": [7.6962, 7.6992],
})

# Title of the app
st.title("Barriera da Migliorare")

# Map visualization
st.subheader("🗺️ 1. Mappa dei Problemi")
st.write("Ecco tutti gli eventi nella tua zona:")
st.write()
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/streets-v11",
    initial_view_state=pdk.ViewState(
        latitude=45.0920,
        longitude=7.6950,
        zoom=15,
        pitch=20,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=events,
            get_position="[Longitude, Latitude]",
            get_color="[200, 30, 0, 160]",
            get_radius=20,
        ),
    ],
))
    
# Proponi due itinerari dettagliati su come raggiungere gli eventi, dettagliando i mezzi di trasporto e i tempi di percorrenza
st.subheader("Problemi evidenziati")
st.write("Ecco i problemi evidenziati dagli abitanti del quartiere:")
st.write("1. Piazza Baldissera")
st.write("   - 🚊 Traffico congestionato")
st.write("   - ⌚ Ritardi costanti dei mezzi pubblici")
st.write("2. Fabbrica abbandonata ex-Gondrand:")
st.write("   - 🏭 Spazio urbano inaccessibile e inquinato")
st.write("   - 🌳 Potenziale area per nuovo parco pubblico")

# File uploader for new events
st.subheader("✏️ 2. Segnala un problema")
# Create a form to upload a problem, their location, and a description
with st.form(key='problem_form'):
    problem_location = st.text_input("Dove si trova il problema?")
    problem_description = st.text_area("Descrivi il problema:")
    submit_button = st.form_submit_button(label='Invia Problema')

# Proponiti come volontario
st.subheader("🤝 3. Proponiti come volontario")
# Create a form to sign up as a volunteer
with st.form(key='volunteer_form'):
    volunteer_name = st.text_input("Nome:")
    volunteer_email = st.text_input("Email:")
    volunteer_availability = st.text_area("Disponibilità:")
    volunteer_skills = st.text_area("Competenze:")
    submit_button = st.form_submit_button(label='Invia candidatura')
