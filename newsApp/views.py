from django.shortcuts import render
from newsapi import NewsApiClient


# HOME
def Index(request):
    newsapi = NewsApiClient(api_key="ef60c58133a540d78da1244df634f8f1")

    sports_headlines = newsapi.get_everything(
        q='sports', domains='si.com', language='en', sort_by='relevancy', page_size=5)
    business_headlines = newsapi.get_everything(
        q='business', domains='cnbc.com', language='en', sort_by='relevancy', page_size=5)
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

    return render(request, 'newsApp/index.html', context={"all_list": all_list})


# SPORTS
def Sports(request):
    newsapi = NewsApiClient(api_key="ef60c58133a540d78da1244df634f8f1")
    
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
    return render(request, 'newsApp/sports.html', context={"sports_list": sports_list})

# BUSINESS
def Business(request):
    newsapi = NewsApiClient(api_key="ef60c58133a540d78da1244df634f8f1")
    
    business1_headline = newsapi.get_everything(
    q='business', domains='cnn.com', language='en', sort_by='relevancy', page_size=5)
    business2_headline = newsapi.get_everything(
    q='business', domains='cnbc.com', language='en', sort_by='relevancy', page_size=5)
    business3_headline = newsapi.get_everything(
    q='business', domains='businessinsider.com', language='en', sort_by='relevancy', page_size=5)
    business4_headline = newsapi.get_everything(
    q='business', domains='forbes.com', language='en', sort_by='relevancy', page_size=5)

    business1_articles = business1_headline['articles']
    business2_articles = business2_headline['articles']
    business3_articles = business3_headline['articles']
    business4_articles = business4_headline['articles']

    business1_desc = []
    business1_news = []
    business1_img = []
    business1_link = []
    business2_desc = []
    business2_news = []
    business2_img = []
    business2_link = []
    business3_desc = []
    business3_news = []
    business3_img = []
    business3_link = []
    business4_desc = []
    business4_news = []
    business4_img = []
    business4_link = []

    for business1_i in range(len(business1_articles)):
        business1_myarticles = business1_articles[business1_i]
        business1_news.append(business1_myarticles['title'])
        business1_desc.append(business1_myarticles['description'])
        business1_img.append(business1_myarticles['urlToImage'])
        business1_link.append(business1_myarticles['url'])

    for business2_i in range(len(business2_articles)):
            business2_myarticles = business2_articles[business2_i]
            business2_news.append(business2_myarticles['title'])
            business2_desc.append(business2_myarticles['description'])
            business2_img.append(business2_myarticles['urlToImage'])
            business2_link.append(business2_myarticles['url'])

    for business3_i in range(len(business3_articles)):
            business3_myarticles = business3_articles[business3_i]
            business3_news.append(business3_myarticles['title'])
            business3_desc.append(business3_myarticles['description'])
            business3_img.append(business3_myarticles['urlToImage'])
            business3_link.append(business3_myarticles['url'])

    for business4_i in range(len(business4_articles)):
            business4_myarticles = business4_articles[business4_i]
            business4_news.append(business4_myarticles['title'])
            business4_desc.append(business4_myarticles['description'])
            business4_img.append(business4_myarticles['urlToImage'])
            business4_link.append(business4_myarticles['url'])
            
    business_list = zip(business1_news, business1_desc, business1_img,business1_link, business2_news, business2_desc, business2_img,business2_link,business3_news, business3_desc, business3_img,business3_link, business4_news, business4_desc, business4_img, business4_link)
    return render(request, 'newsApp/business.html', context={"business_list": business_list})

# TECH
def Tech(request):
    newsapi = NewsApiClient(api_key="ef60c58133a540d78da1244df634f8f1")
    
    tech1_headline = newsapi.get_everything(
    q='technology', domains='bleepingcomputer.com', language='en', sort_by='relevancy', page_size=5)
    tech2_headline = newsapi.get_everything(
    q='technology', domains='techcrunch.com', language='en', sort_by='relevancy', page_size=5)
    tech3_headline = newsapi.get_everything(
    q='technology', domains='theverge.com', language='en', sort_by='relevancy', page_size=5)
    tech4_headline = newsapi.get_everything(
    q='technology', domains='venturebeat.com', language='en', sort_by='relevancy', page_size=5)

    tech1_articles = tech1_headline['articles']
    tech2_articles = tech2_headline['articles']
    tech3_articles = tech3_headline['articles']
    tech4_articles = tech4_headline['articles']

    tech1_desc = []
    tech1_news = []
    tech1_img = []
    tech1_link = []
    tech2_desc = []
    tech2_news = []
    tech2_img = []
    tech2_link = []
    tech3_desc = []
    tech3_news = []
    tech3_img = []
    tech3_link = []
    tech4_desc = []
    tech4_news = []
    tech4_img = []
    tech4_link = []

    for tech1_i in range(len(tech1_articles)):
        tech1_myarticles = tech1_articles[tech1_i]
        tech1_news.append(tech1_myarticles['title'])
        tech1_desc.append(tech1_myarticles['description'])
        tech1_img.append(tech1_myarticles['urlToImage'])
        tech1_link.append(tech1_myarticles['url'])

    for tech2_i in range(len(tech2_articles)):
            tech2_myarticles = tech2_articles[tech2_i]
            tech2_news.append(tech2_myarticles['title'])
            tech2_desc.append(tech2_myarticles['description'])
            tech2_img.append(tech2_myarticles['urlToImage'])
            tech2_link.append(tech2_myarticles['url'])

    for tech3_i in range(len(tech3_articles)):
            tech3_myarticles = tech3_articles[tech3_i]
            tech3_news.append(tech3_myarticles['title'])
            tech3_desc.append(tech3_myarticles['description'])
            tech3_img.append(tech3_myarticles['urlToImage'])
            tech3_link.append(tech3_myarticles['url'])

    for tech4_i in range(len(tech4_articles)):
            tech4_myarticles = tech4_articles[tech4_i]
            tech4_news.append(tech4_myarticles['title'])
            tech4_desc.append(tech4_myarticles['description'])
            tech4_img.append(tech4_myarticles['urlToImage'])
            tech4_link.append(tech4_myarticles['url'])
            
    tech_list = zip(tech1_news, tech1_desc, tech1_img,tech1_link, tech2_news, tech2_desc, tech2_img,tech2_link,tech3_news, tech3_desc, tech3_img,tech3_link, tech4_news, tech4_desc, tech4_img, tech4_link)
    return render(request, 'newsApp/tech.html', context={"tech_list": tech_list})

# SCIENCE
def Science(request):
    newsapi = NewsApiClient(api_key="ef60c58133a540d78da1244df634f8f1")
    
    science1_headline = newsapi.get_everything(
    q='science', domains='atlasobscura.com', language='en', sort_by='relevancy', page_size=5)
    science2_headline = newsapi.get_everything(
    q='science', domains='livescience.com', language='en', sort_by='relevancy', page_size=5)
    science3_headline = newsapi.get_everything(
    q='science', domains='arstechnica.com', language='en', sort_by='relevancy', page_size=5)
    science4_headline = newsapi.get_everything(
    q='science', domains='nationalgeographic.com', language='en', sort_by='relevancy', page_size=5)

    science1_articles = science1_headline['articles']
    science2_articles = science2_headline['articles']
    science3_articles = science3_headline['articles']
    science4_articles = science4_headline['articles']

    science1_desc = []
    science1_news = []
    science1_img = []
    science1_link = []
    science2_desc = []
    science2_news = []
    science2_img = []
    science2_link = []
    science3_desc = []
    science3_news = []
    science3_img = []
    science3_link = []
    science4_desc = []
    science4_news = []
    science4_img = []
    science4_link = []

    for science1_i in range(len(science1_articles)):
        science1_myarticles = science1_articles[science1_i]
        science1_news.append(science1_myarticles['title'])
        science1_desc.append(science1_myarticles['description'])
        science1_img.append(science1_myarticles['urlToImage'])
        science1_link.append(science1_myarticles['url'])

    for science2_i in range(len(science2_articles)):
            science2_myarticles = science2_articles[science2_i]
            science2_news.append(science2_myarticles['title'])
            science2_desc.append(science2_myarticles['description'])
            science2_img.append(science2_myarticles['urlToImage'])
            science2_link.append(science2_myarticles['url'])

    for science3_i in range(len(science3_articles)):
            science3_myarticles = science3_articles[science3_i]
            science3_news.append(science3_myarticles['title'])
            science3_desc.append(science3_myarticles['description'])
            science3_img.append(science3_myarticles['urlToImage'])
            science3_link.append(science3_myarticles['url'])

    for science4_i in range(len(science4_articles)):
            science4_myarticles = science4_articles[science4_i]
            science4_news.append(science4_myarticles['title'])
            science4_desc.append(science4_myarticles['description'])
            science4_img.append(science4_myarticles['urlToImage'])
            science4_link.append(science4_myarticles['url'])
            
    science_list = zip(science1_news, science1_desc, science1_img,science1_link, science2_news, science2_desc, science2_img,science2_link,science3_news, science3_desc, science3_img,science3_link, science4_news, science4_desc, science4_img, science4_link)
    return render(request, 'newsApp/science.html', context={"science_list": science_list})

    # ENTERTAINMENT
def Entertainment(request):
    newsapi = NewsApiClient(api_key="ef60c58133a540d78da1244df634f8f1")
    
    entertainment1_headline = newsapi.get_everything(
    q='entertainment', domains='avclub.com', language='en', sort_by='relevancy', page_size=5)
    entertainment2_headline = newsapi.get_everything(
    q='entertainment', domains='variety.com', language='en', sort_by='relevancy', page_size=5)
    entertainment3_headline = newsapi.get_everything(
    q='entertainment', domains='deadline.com', language='en', sort_by='relevancy', page_size=5)
    entertainment4_headline = newsapi.get_everything(
    q='entertainment', domains='latimes.com', language='en', sort_by='relevancy', page_size=5)

    entertainment1_articles = entertainment1_headline['articles']
    entertainment2_articles = entertainment2_headline['articles']
    entertainment3_articles = entertainment3_headline['articles']
    entertainment4_articles = entertainment4_headline['articles']

    entertainment1_desc = []
    entertainment1_news = []
    entertainment1_img = []
    entertainment1_link = []
    entertainment2_desc = []
    entertainment2_news = []
    entertainment2_img = []
    entertainment2_link = []
    entertainment3_desc = []
    entertainment3_news = []
    entertainment3_img = []
    entertainment3_link = []
    entertainment4_desc = []
    entertainment4_news = []
    entertainment4_img = []
    entertainment4_link = []

    for entertainment1_i in range(len(entertainment1_articles)):
        entertainment1_myarticles = entertainment1_articles[entertainment1_i]
        entertainment1_news.append(entertainment1_myarticles['title'])
        entertainment1_desc.append(entertainment1_myarticles['description'])
        entertainment1_img.append(entertainment1_myarticles['urlToImage'])
        entertainment1_link.append(entertainment1_myarticles['url'])

    for entertainment2_i in range(len(entertainment2_articles)):
            entertainment2_myarticles = entertainment2_articles[entertainment2_i]
            entertainment2_news.append(entertainment2_myarticles['title'])
            entertainment2_desc.append(entertainment2_myarticles['description'])
            entertainment2_img.append(entertainment2_myarticles['urlToImage'])
            entertainment2_link.append(entertainment2_myarticles['url'])

    for entertainment3_i in range(len(entertainment3_articles)):
            entertainment3_myarticles = entertainment3_articles[entertainment3_i]
            entertainment3_news.append(entertainment3_myarticles['title'])
            entertainment3_desc.append(entertainment3_myarticles['description'])
            entertainment3_img.append(entertainment3_myarticles['urlToImage'])
            entertainment3_link.append(entertainment3_myarticles['url'])

    for entertainment4_i in range(len(entertainment4_articles)):
            entertainment4_myarticles = entertainment4_articles[entertainment4_i]
            entertainment4_news.append(entertainment4_myarticles['title'])
            entertainment4_desc.append(entertainment4_myarticles['description'])
            entertainment4_img.append(entertainment4_myarticles['urlToImage'])
            entertainment4_link.append(entertainment4_myarticles['url'])
            
    entertainment_list = zip(entertainment1_news, entertainment1_desc, entertainment1_img,entertainment1_link, entertainment2_news, entertainment2_desc, entertainment2_img,entertainment2_link,entertainment3_news, entertainment3_desc, entertainment3_img,entertainment3_link, entertainment4_news, entertainment4_desc, entertainment4_img, entertainment4_link)
    return render(request, 'newsApp/entertainment.html', context={"entertainment_list": entertainment_list})