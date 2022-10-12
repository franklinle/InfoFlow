from django.shortcuts import render
from newsapi import NewsApiClient


def Index(request):
    newsapi = NewsApiClient(api_key="52bf227da152410f9d1ad5ef014b27f3")

    sportsheadlines = newsapi.get_everything(q='sports',
                                             domains='espn.com',
                                             language='en',
                                             sort_by='relevancy',
                                             page_size=15)

    articles = sportsheadlines['articles']

    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, img, link)

    return render(request, 'index.html', context={"mylist": mylist})
