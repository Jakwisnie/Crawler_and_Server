import requests
from requests_html import HTMLSession

session = HTMLSession()
    
url ='https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[B]'

r =  session.get(url)
r.html.render(sleep =1 ,scrolldown = 5)

articles = r.html.find('tr class="cardItem oddItem"')
newslist = []

for item in articles:
    try:
        newsitem = item.find('span class = "cardInfo"',first=True)
        newsarticle = {
        'title' : newsitem.text,
        'link' : newsitem.rulesText
        }
        newslist.append(newsarticle)
    except:
        pass
    
print(newslist)