from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

quotes_page ='https://bluelimelearning.github.io/my-fav-quotes/'

uClient=uReq(quotes_page)
page_html=uClient.read()
uClient.close()
page_soup=BeautifulSoup(page_html, "html.parser")

#mulai ambil dari classnya css
quotes = page_soup.findAll("div",{"class":"quotes"})

for quote in quotes:
    fav_qoute=quote.findAll("p",{"class":"aquote"})
    aquote=fav_qoute[0].text.strip() 

    fav_author=quote.findAll("p",{"class":"author"})
    author=fav_qoute[0].text.strip()

    print(aquote)
    print(author)
    