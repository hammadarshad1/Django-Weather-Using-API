from django.shortcuts import render
import requests
from .models import *
from .forms import *

# Create your views here.
def home(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=a930e212fcaf72a16023e45a0f2d6b1f'
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    weather_data = []
    for city in cities:
        data = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    return render(request, 'weather/weather.html', {'weather_data':weather_data, 'form':form})