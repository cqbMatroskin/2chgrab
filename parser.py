from bs4 import BeautifulSoup

import constants


def get_links(html, limit=None):
    soup = BeautifulSoup(html, "lxml")
    content = soup.findAll('a', attrs='post__image-link')
    links = []
    for post in content:
        if len(links) < limit:
            if not ('mp4' or 'webm') in post.get('href'):
                links.append(constants.BASE_URL + post.get('href'))
    return links
