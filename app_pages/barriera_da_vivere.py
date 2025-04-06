import streamlit as st
import pandas as pd
import pydeck as pdk

# Placeholder dataset for events
events = pd.DataFrame({
    "Categoria": ["Musica", "Arte", "Letteratura"],
    "Nome Evento": ["Kappa Future Festival", "TOdays", "Salone del Libro OFF"],
    "Indirizzo": ["Parco Dora, Torino", "Spazio 211", "SNOS"],
    "Latitude": [45.0918, 45.0924, 45.0934],
    "Longitude": [7.6962, 7.6912, 7.6992],
})

# Title of the app
st.title("Barriera da Vivere")

# User query input
st.subheader("1. Cosa ti interessa?")
st.write("🤌 Prova qualcosa come 'Letteratura', 'Musica' o 'Arte'!")
query = st.text_input("Chiedimi qualunque informazione sugli eventi nel tuo quartiere!")

# Display events matching the query
if query:
    filtered_events = events[events["Categoria"].str.contains(query, case=False)]
    if not filtered_events.empty:
        st.write("Ecco gli eventi più interessanti per te:")
        st.write(filtered_events[["Categoria", "Nome Evento", "Indirizzo"]])
    else:
        st.write("No events found.")

# Map visualization
st.subheader("Mappa degli Eventi")
st.write("Ecco tutti gli eventi nella tua zona:")
st.write()
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/streets-v11",
    initial_view_state=pdk.ViewState(
        latitude=45.0920,
        longitude=7.6950,
        zoom=45,
        pitch=20,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=events,
            get_position="[Longitude, Latitude]",
            get_color="[200, 30, 0, 160]",
            get_radius=50,
        ),
    ],
))

# Proponi due itinerari dettagliati su come raggiungere gli eventi, dettagliando i mezzi di trasporto e i tempi di percorrenza
st.subheader("Ecco tutti gli eventi nella tua zona:")
st.write(events[["Categoria", "Nome Evento", "Indirizzo"]])

# File uploader for new events
st.subheader("2. Carica il tuo Evento!")
uploaded_file = st.file_uploader("Carica la descrizione del tuo evento", type=["csv"])

if uploaded_file:
    new_events = pd.read_csv(uploaded_file)
    events = pd.concat([events, new_events], ignore_index=True)
    st.success("Your event has been added!")
