import streamlit as st
import seaborn as sns
import pandas as pd
import datetime as dt
import plotly.express as px
import requests

class WeatherServices:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city_name):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}&units=metric&lang=en"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            st.error(f"An error fetching current weather {e} occurred", icon="😵")
            return None

    def get_forecast(self, city_name):
        url= f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={self.api_key}&units=metric"
        try:
            response=requests.get(url, timeout =5)
            if response.status_code == 200:
               return response.json()
            else:
                return None
        except Exception as e:
            st.error(f"error fetching forecast {e} occurred")
            return None



    @staticmethod #func gets text and the output is an emoji
    def formatted_description(description_text):
        desc = description_text.lower()
        if "cloud" in desc:
            weather_icon = "☁️"
        elif "rain" in desc:
            weather_icon = "🌧"
        elif "sun" in desc:
            weather_icon = "☀️"
        elif "snow" in desc:
            weather_icon = "❄️"
        else:
            weather_icon = "⛅️"
        return weather_icon

    @staticmethod
    def clothing_advice(feels_like_temp): #get an integer only and the output  is a string
        if feels_like_temp<15:
            return "Its freezing, wear a coat 🧥🧣"
        elif 15<=feels_like_temp<22:
            return "It's a bit chilly, take a light jacket with you 🧥 "
        elif 22<=feels_like_temp<30:
            return "Perfect weather ahead! wear a t-shirt 👕 "
        else:
            return "Extreme heat outside, wear a tank top 🎽"


weather_tool = WeatherServices(st.secrets["weather_api_key"])
st.title("My weather 🏖 ")

city = st.text_input("Please enter the current city name", "Jerusalem")

if st.button("Search"):
    data = weather_tool.get_weather(city)

    if data:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        raw_desc = data['weather'][0]["description"]
        current_icon = weather_tool.formatted_description(raw_desc)

        st.success(f"The values of {city} were received successfully")

        feels_like=data['main']['feels_like']
        advice =weather_tool.clothing_advice(feels_like)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Temperature 🔥", f"{temp}°C")
        col2.metric("Humidity 💧", f"{humidity}%")
        col3.metric("Condition", current_icon)
        col4.metric("It's feels like", f"{feels_like}")
        st.info(f"The system recommendation is {advice}")


        forecast_data = weather_tool.get_forecast(city)

        if forecast_data:

            df=pd.DataFrame(forecast_data['list'])
            df['time']=pd.to_datetime(df['dt_txt'])
            df['temp']=df['main'].apply(lambda x:x['temp']) #extracting the temp column
            df['humidity']=df['main'].apply(lambda x:x['humidity']) #extracting the humidity column
            df['description']=df['weather'].apply(lambda x: x[0]['description']) #getting the description from the first call of the list
            fig=px.scatter(df, x="time", y="temp", hover_data=['humidity','description'], color_continuous_scale="bluered") #building the graph and his components
            st.plotly_chart(fig, use_container_width=True) #display the graph to the user adding color
            fig.update_traces(mode='lines+markers') #connecting the dots and makes the color change visible


            list_of_forecasts = forecast_data['list']
            st.write(f"I have got {len(list_of_forecasts)} forecasts")
            if forecast_data:
                list_of_forecasts = forecast_data['list']

                # חילוץ הטמפרטורות מתוך 40 התחזיות
                temps = []
                for item in list_of_forecasts:
                    temps.append(item['main']['temp'])

                st.markdown("---")
                st.subheader("Weekly Temperature Forecast") #subtitle

                # הצגת הגרף
                st.line_chart(temps)
            else:
                st.warning("Could not pull out the forecast data")
        else:
            st.warning("Could not pull out the forecast data")
    else:
        st.error("Could not find the specific city you have entered")