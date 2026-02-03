
## Interactive Weather App🌅

A dynamic weather app built with Python and Streamlit. You can watch the Live Demo here: https://pythonproject2-gczpgoqzirkkno96ddviir.streamlit.app/
The app leverages the OpenWeatherMap API to provide real time 
weather data and a 5 day forecast for any city worldwide.

## Key features:
1. Real time data displays:  *current temperature, *humidity *weather conditions (e.g clouds,rain,sun etc.)
2. Smart clothing advice: analyzes the "Feels Like" temperature to provide personalized recommendations on what to
wear.
3. Dynamic visualizations: Uses "Plotly" to create interactive scatter plots  showing temperature and humidity trends.
4. 5 Day Forecast: visualizes upcoming temperature trends with clean line chart

## Tech stack 💻:
1. Streamlit for the web interface
2. Pandas for data manipulation and analysis
3. Plotly and Seaborn for interactive and static visualizations
4. Requests: For handling HTTP API calls


## Installation and Setup ⚙️:
```bash
git clone https://github.com/ranel-star/PythonProject2.git
```


## Install Dependencies:
```pip install -r requirements.txt
```


## API configurations:
Create a folder named .streamlit and a file inside calls secrets.toml. Add your OpenWeatherMap API key:
```Your_API_Key
```


## Run the app
```streamlit run main.py 
```