from bs4 import BeautifulSoup
import requests

import constants


def get_links(html, limit=None):
    soup = BeautifulSoup(html, "lxml")
    content = soup.findAll('a', attrs='post__image-link', limit=limit)
    links = []
    for post in content:
        links.append(constants.BASE_URL + post.get('href'))
    return links
