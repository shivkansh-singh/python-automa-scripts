import requests
import sys

zipcode = input("Enter the zip code: ")
countrycode = input("Enter your country code: ")
apikey="1eb0d3498a7333f8a01072325a17d3d0"
#6b970fab4b35817499b86ddcf0b2b437
weather_url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={apikey}"

result = requests.get(weather_url)

if result.status_code !=200:
  print("Error: Something went wrong. Please try again")
  sys.exit(1)
else:
  print(result.json())
  sys.exit(0)
