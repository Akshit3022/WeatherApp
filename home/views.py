from django.shortcuts import render
import requests 

# Create your views here.


def home(request):

    city = request.GET.get('city', "Surat")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1db7ba126895ddf5ea0b981f35b8c2b6'
    data = requests.get(url).json()
    # print(data) 

    try:
        payload = {
            'city': data.get('name', 'City Not Found'), 
            'weather': data['weather'][0]['main'], 
            'icon': data['weather'][0]['icon'],
            'kelvin_temperature': data['main']['temp'], 
            'celcius_temperature': int(data['main']['temp'] - 273), 
            'pressure': data['main']['pressure'], 
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }

        context = {'data': payload}
    except KeyError:
        # Handle the KeyError here, e.g., by providing a default error message
        error_message = "Error: City not found, try to enter correct name."
        context = {'error_message': error_message}

    return render(request, 'home.html', context)