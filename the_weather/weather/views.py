from django.shortcuts import render
import requests
from .models import City
from .forms import city_name



def index(request):
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&APPID=4e3aadd76d19d3209156dccbff340001'

    form = city_name(request.POST)
    if request.method == 'POST':

        if form.is_valid():
           city = form.cleaned_data['name']
    else:
        city = "Mumbai" #Default City


    r = requests.get(url.format(city)).json()
    context = {
        'city'        : city,
        'temperature' : r['list'][0]['main']['temp'],
        'describe'    : r['list'][0]['weather'][0]['description'] ,
        'pressure'    : r['list'][0]['main']['pressure'],
        'sea_level'   : r['list'][0]['main']['sea_level'],
        'humidity'    : r['list'][0]['main']['humidity'],
        'form'        : form,
    }

    return render(request,'weather/index.html',context = context)


def forms_view(request):
    form = forms.city_name()
    return render(request,'weather/forms.html',{'form' : form })
