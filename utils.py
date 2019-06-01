import requests
import os
import uuid
import time

import constants
import parser

# def enter_data():
#
#     if photo_limit != '':
#
#     return url, photo_limit


def get_page(thread):
    url = constants.BASE_URL + thread
    response = requests.get(url, headers={"user-agent": constants.USER_AGENT})
    response.raise_for_status()
    return response.content


def parse_page(html, limit=None):
    links = parser.get_links(html, limit)
    if not links:
        print('Не удалось получить ссылки')
        return
    else:
        return links


def create_directory():
    dir_name = input('Enter directory name ')
    dir_name.strip().replace(' ', '_')
    if not os.path.exists(constants.DOWNLOAD_PATH.format(dir_name)):
        os.mkdir(constants.DOWNLOAD_PATH.format(dir_name))
        name = constants.DOWNLOAD_PATH.format(dir_name)
        print('Directory {} is created'.format(dir_name))
        return name


def dl_image(links, sleep=1):
    path = create_directory()
    print('Download {} images ...'.format(len(links)))
    for link in links:
        image = requests.get(link)
        with open(path + '/{0}.jpg'.format(uuid.uuid4().hex), 'wb') as temp_file:
            temp_file.write(image.content)
        time.sleep(sleep)
