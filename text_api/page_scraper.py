import re
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as soup


def clean_up_text(text):
    return re.sub(u"(\u2018|\u2019)", "'", text)


def scrape_url(url, tag_attributes=None):
    web_page = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()
    page_soup = soup(web_page, "html.parser")
    paragraphs = page_soup.find_all('p', attrs={'class': tag_attributes})
    article_text = ""
    for paragraph in paragraphs:
        article_text += paragraph.text
    return clean_up_text(article_text)
