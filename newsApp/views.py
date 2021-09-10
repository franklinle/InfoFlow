from django.shortcuts import render
from newsapi import NewsApiClient
 
 
 
def Index(request):
    newsapi = NewsApiClient(api_key="52bf227da152410f9d1ad5ef014b27f3")
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')
 
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
 
    mylist = zip(news, desc, img)
 
 
    return render(request, 'index.html', context={"mylist":mylist})
 
 
 
def bbc(request):
    newsapi = NewsApiClient(api_key="52bf227da152410f9d1ad5ef014b27f3")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')
 
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
 
    mylist = zip(news, desc, img)
 
 
    return render(request, 'bbc.html', context={"mylist":mylist})