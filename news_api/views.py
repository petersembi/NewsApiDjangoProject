from django.shortcuts import render
import requests
API_KEY = 'b500a97ea65e4f4f8a9fac6749909a0f'

# Create your views here.

def home(request):
    # the f here enables it to accept the api key dynamically
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    
    # to change data to json
    data = response.json()
    # print(data)
    articles = data['articles']
    

    context = {
        'articles' : articles
    }

    return render(request, 'news_api/home.html', context)
    