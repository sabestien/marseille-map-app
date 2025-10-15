import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- App Title ---
st.title("🗺️ Marseille Locations Map")

# --- Load Data ---
try:
    # Load the Excel file
    df = pd.read_excel("Listing_Marseille_2.xlsx")

    # Check if essential columns exist
    if 'latitude' not in df.columns or 'longitude' not in df.columns:
        st.error("Error: Your Excel file must have 'latitude' and 'longitude' columns.")
    else:
        # --- Create Map ---
        map_center = [df['latitude'].mean(), df['longitude'].mean()]
        m = folium.Map(location=map_center, zoom_start=13)

        # --- Add Markers to the Map ---
        st.write("Adding location markers to the map...")

        for idx, row in df.iterrows():
            hover_text = row.get('adresse_complete', 'Address not available')
            popup_title = row.get('Adresse recherchée', hover_text)

            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=5,
                color='red',
                fill=True,
                fill_color='red',
                fill_opacity=0.7,
                popup=f"<b>{popup_title}</b>",
                tooltip=hover_text
            ).add_to(m)

        # --- Display the Map in Streamlit ---
        st_folium(m, width=800, height=600)

        # --- (Optional) Display Raw Data ---
        if st.checkbox("Show raw data from Excel"):
            st.dataframe(df)

except FileNotFoundError:
    st.error("Error: The file 'Listing_Marseille_2.xlsx' was not found. Please place it in the same directory.")
except Exception as e:
    st.error(f"An error occurred: {e}")