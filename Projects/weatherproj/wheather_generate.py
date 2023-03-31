import requests

API_key="bacbcdc2a59e1b0e1e8e2c43d60960c1"
city_name=input("city name: ")


API_request=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
response=requests.get(API_request)

if response.status_code==200:
    data=response.json()
    print("complete data:\n",data)
    weather_desc=data['weather'][0]['description']
    print("\nweather: ", weather_desc)
    temperature=data['main']['temp'] - 273.15
    print("temperature: ", temperature, "celsius")
    humidity=data['main']['humidity']
    print("humidity: ", humidity)
else:
    print("an error occured")
