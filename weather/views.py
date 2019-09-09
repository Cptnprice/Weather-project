from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
# Create your views here.

def home(request):
    return render(request,'home.html')

def get_weather(request):
    city_name = request.POST['city_name']
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=10bfc032bb911a982d846dbebeca28b1'.format(city_name)
    r = requests.get(url).json()
    if r['cod'] == '404' or not city_name:
        return render(request,'home.html',{'error' : 'Please, enter correct city name'})
    city_weather = {
        'city_name' : city_name,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon']
    }
    context = {'city_weather' : city_weather}
    return render(request,'weather.html',context)
