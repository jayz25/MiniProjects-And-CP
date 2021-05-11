from django.shortcuts import render
import json
# Create your views here.
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=484449c16a0c01f4ef79c670a0a1b616'
        source = urllib.request.urlopen(url.format(city)).read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon'])+ ' '+
                            str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp'])+ 'K',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html",data)

