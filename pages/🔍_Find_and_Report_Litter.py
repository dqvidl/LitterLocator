import streamlit as st
import pandas as pd
import requests
import numpy as np
from geopy.geocoders import Nominatim
from streamlit_extras.app_logo import add_logo


st.set_page_config(
  page_title = "Find and Report Litter - Litter Locator",
  page_icon = "🌲",
  layout = "wide"
) 


add_logo("https://cdn.discordapp.com/attachments/534885876585725985/1147776610834071572/logo-removebg-preview.png")

st.header("Report Litter")
st.write("Report litter polluted areas")

dfReport = pd.DataFrame(columns=["Address", "Latitude", "Longitude"])
address = st.text_input("Your Address or Location")

st.subheader("Picture")

pictureorno = st.selectbox("Would you like to provide a photograph of of the region to help locate the polluted area?", ('Select', 'Yes', 'No'))

if pictureorno == 'Yes':
  pictureOption = st.selectbox("Choose:", ('', 'Choose Photo from Library', 'Take Picture'))
  if pictureOption == 'Take Picture':
    picture = st.camera_input("Take a picture")
    if picture:
      st.image(picture)
  elif pictureOption == 'Choose Photo from Library':
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)

finished = False
if address != '':
    finished = True

if st.button("Submit", disabled = not finished):
       if address:
        geolocator = Nominatim(user_agent="address-to-coordinates-converter")
        try:
            location = geolocator.geocode(address)

            if location:
                latitude = location.latitude
                longitude = location.longitude
                st.success(f"Latitude: {latitude}, Longitude: {longitude}")
                st.write("Thank You :)")
                st.write("Your contributions will direct us towards a greener planet!")
            else:
                st.error("Address not found. Please enter a valid address.")
        except Exception as e2:
            st.error(f"An error occurred: {str(e2)}")


st.divider()

st.header("Find Litter")
st.write("Search for litter polluted areas near you")

try:
        map_data = pd.DataFrame(
            np.random.randn(1, 2) / [10000000000,10000000000] + [location.latitude, location.longitude],
            columns=['lat', 'lon'])
        st.map(map_data)
except Exception as e:
        st.map()
