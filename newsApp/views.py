from django.shortcuts import render
from newsapi import NewsApiClient


# SPORTS
def Index(request):
    newsapi = NewsApiClient(api_key="52bf227da152410f9d1ad5ef014b27f3")

    sports_headlines = newsapi.get_everything(
        q='sports', domains='espn.com', language='en', sort_by='relevancy', page_size=5)
    business_headlines = newsapi.get_everything(
        q='business', domains='cnbc.com', language='en', sort_by='relevancy', page_size=5)
    tech_headlines = newsapi.get_everything(
        q='technology', domains='theverge.com', language='en', sort_by='relevancy', page_size=5)
    science_headlines = newsapi.get_everything(
        q='science', domains='livescience.com', language='en', sort_by='relevancy', page_size=5)

    sports_articles = sports_headlines['articles']
    business_articles = business_headlines['articles']
    tech_articles = tech_headlines['articles']
    science_articles = science_headlines['articles']

    sports_desc = []
    sports_news = []
    sports_img = []
    sports_link = []
    business_desc = []
    business_news = []
    business_img = []
    business_link = []
    tech_desc = []
    tech_news = []
    tech_img = []
    tech_link = []
    science_desc = []
    science_news = []
    science_img = []
    science_link = []

    for sports_i in range(len(sports_articles)):
        sports_myarticles = sports_articles[sports_i]
        sports_news.append(sports_myarticles['title'])
        sports_desc.append(sports_myarticles['description'])
        sports_img.append(sports_myarticles['urlToImage'])
        sports_link.append(sports_myarticles['url'])

    for business_i in range(len(business_articles)):
        business_myarticles = business_articles[business_i]
        business_news.append(business_myarticles['title'])
        business_desc.append(business_myarticles['description'])
        business_img.append(business_myarticles['urlToImage'])
        business_link.append(business_myarticles['url'])

    for tech_i in range(len(tech_articles)):
        tech_myarticles = tech_articles[tech_i]
        tech_news.append(tech_myarticles['title'])
        tech_desc.append(tech_myarticles['description'])
        tech_img.append(tech_myarticles['urlToImage'])
        tech_link.append(tech_myarticles['url'])

    for science_i in range(len(science_articles)):
        science_myarticles = science_articles[science_i]
        science_news.append(science_myarticles['title'])
        science_desc.append(science_myarticles['description'])
        science_img.append(science_myarticles['urlToImage'])
        science_link.append(science_myarticles['url'])

    all_list = zip(sports_news, sports_desc, sports_img,sports_link, 
    business_news, business_desc, business_img, business_link,
    tech_news, tech_desc, tech_img, tech_link,
    science_news, science_desc, science_img, science_link)

    return render(request, 'index.html', context={"all_list": all_list})
