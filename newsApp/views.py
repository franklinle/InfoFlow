from django.shortcuts import render
from newsapi import NewsApiClient


# HOME
def Index(request):
    newsapi = NewsApiClient(api_key="edf912e806f04213b4f39a3306163433")

    sports_headlines = newsapi.get_everything(
        q='sports', domains='espn.com', language='en', sort_by='relevancy', page_size=5)
    business_headlines = newsapi.get_everything(
        q='business', domains='forbes.com', language='en', sort_by='relevancy', page_size=5)
    tech_headlines = newsapi.get_everything(
        q='technology', domains='venturebeat.com', language='en', sort_by='relevancy', page_size=5)
    science_headlines = newsapi.get_everything(
        q='science', domains='nationalgeographic.com', language='en', sort_by='relevancy', page_size=5)

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


# SPORTS
def Sports(request):
    newsapi = NewsApiClient(api_key="edf912e806f04213b4f39a3306163433")
    
    sports1_headline = newsapi.get_everything(
    q='sports', domains='espn.com', language='en', sort_by='relevancy', page_size=5)
    sports2_headline = newsapi.get_everything(
    q='sports', domains='si.com', language='en', sort_by='relevancy', page_size=5)
    sports3_headline = newsapi.get_everything(
    q='sports', domains='sbnation.com', language='en', sort_by='relevancy', page_size=5)
    sports4_headline = newsapi.get_everything(
    q='sports', domains='deadspin.com', language='en', sort_by='relevancy', page_size=5)

    sports1_articles = sports1_headline['articles']
    sports2_articles = sports2_headline['articles']
    sports3_articles = sports3_headline['articles']
    sports4_articles = sports4_headline['articles']

    sports1_desc = []
    sports1_news = []
    sports1_img = []
    sports1_link = []
    sports2_desc = []
    sports2_news = []
    sports2_img = []
    sports2_link = []
    sports3_desc = []
    sports3_news = []
    sports3_img = []
    sports3_link = []
    sports4_desc = []
    sports4_news = []
    sports4_img = []
    sports4_link = []

    for sports1_i in range(len(sports1_articles)):
        sports1_myarticles = sports1_articles[sports1_i]
        sports1_news.append(sports1_myarticles['title'])
        sports1_desc.append(sports1_myarticles['description'])
        sports1_img.append(sports1_myarticles['urlToImage'])
        sports1_link.append(sports1_myarticles['url'])

    for sports2_i in range(len(sports2_articles)):
            sports2_myarticles = sports2_articles[sports2_i]
            sports2_news.append(sports2_myarticles['title'])
            sports2_desc.append(sports2_myarticles['description'])
            sports2_img.append(sports2_myarticles['urlToImage'])
            sports2_link.append(sports2_myarticles['url'])

    for sports3_i in range(len(sports3_articles)):
            sports3_myarticles = sports3_articles[sports3_i]
            sports3_news.append(sports3_myarticles['title'])
            sports3_desc.append(sports3_myarticles['description'])
            sports3_img.append(sports3_myarticles['urlToImage'])
            sports3_link.append(sports3_myarticles['url'])

    for sports4_i in range(len(sports4_articles)):
            sports4_myarticles = sports4_articles[sports4_i]
            sports4_news.append(sports4_myarticles['title'])
            sports4_desc.append(sports4_myarticles['description'])
            sports4_img.append(sports4_myarticles['urlToImage'])
            sports4_link.append(sports4_myarticles['url'])
            
    sports_list = zip(sports1_news, sports1_desc, sports1_img,sports1_link, sports2_news, sports2_desc, sports2_img,sports2_link,sports3_news, sports3_desc, sports3_img,sports3_link, sports4_news, sports4_desc, sports4_img, sports4_link)
    return render(request, 'sports.html', context={"sports_list": sports_list})