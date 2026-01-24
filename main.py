import seaborn as sns
import pandas as pd
import streamlit as st
import requests

st.title("My weather 🏖 ")
citu = st.text_input("Please enter the current city name", "Jerusalem")  # Default city name is Jerusalem
API_KEY = st.secrets["weather_api_key"]  # in a unique folder
url = f"https://api.openweathermap.org/data/2.5/weather?q={citu}&appid={API_KEY}&units=metric&lang=en"  # q-query asks for the city name, appid-specific app id, units in kelvin as default
if st.button("Search"):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        st.success(f"The values of {citu} was received successfully")
        col1, col2 = st.columns(2)
        col1.metric("Temperature 🔥 is", f"{temp}°C")
        col2.metric("Humidity 💧 is", f"{humidity}%")
    else:
        st.error("Could not find the specific city you have entered")



