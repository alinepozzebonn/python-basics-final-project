#import all the libraries that will be used
import requests
from rich import print
from datetime import datetime 

#functions that will be used in the weather application
def welcome():
  """Display welcome message"""
print("[purple]Welcome to my weather app[/purple]")

def display_temperature(day, temperature, unit='ºC'): 
  """Display the current weather information for a given city"""
  #If the temperature if equal or above 20, then it will be in a color different than if the temperature is less than 20ºC. 
  if temperature>= 20:
    print(f"{day}: [dark_orange3]{round(temperature)}{unit}[/dark_orange3]")
  else: 
    print(f"{day}: [light_sea_green]{round(temperature)}{unit}[/light_sea_green]")

def display_weather(city):
  """Display the current weather information for a given city"""
  api_key = "0c62c805ob60a47dat87b32b5f7fb155"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

  #In order to have the information we need, we need to read it as json
  response = requests.get(api_url)
  weather_information = response.json()
  
  #We will access the data and assign it to variable 
  city_name = weather_information['city']
  current_temperature = weather_information['temperature']['current']

  display_temperature("[medium_purple2 bold]Today[/medium_purple2 bold]", (current_temperature))

def display_forecast(city):
  """Display the weather forecast information for a given city"""
  api_key = "0c62c805ob60a47dat87b32b5f7fb155"
  api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}"
  print("\n[medium_purple2 bold]Forecast:[/medium_purple2 bold]")
  response = requests.get(api_url)
  forecast_information = response.json()
  
  #In order to display the forecast, we need to access the data and in a loop get information about each day and it's temperature forecast 
  for day in forecast_information['daily']:
   timestamp = day['time']  
   date = datetime.fromtimestamp(timestamp)
   formatted_day = date.strftime("%A")
   temperature = day['temperature']['day']

   if date.date() != datetime.today().date():
      display_temperature(formatted_day, round(temperature))



welcome()
#In order to have the city, we need to ask the user: 
city_name = input("Enter a city name: ")
city_name = city_name.strip()
#Validation: if the user does not enter a city, the program will ask again
if city_name:
  display_weather(city_name)
  display_forecast(city_name)

else:
  print("Please, enter a valid city name.")


print("\n[light_pink3]This app was built by Aline Pozzebon[/light_pink3]")