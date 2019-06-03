import requests
import os
import uuid
import re
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
    dir_name = constants.DOWNLOAD_PATH.format(time.strftime('%Y-%m-%d'))
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print('Directory {} is created'.format(dir_name))
    return dir_name


def dl_image(links, sleep=1):
    path = create_directory()
    pattern = re.compile('(jpg|jpeg|png)')
    print('Download {} images ...'.format(len(links)))
    for link in links:
        image = requests.get(link)
        image_type = image.headers['Content-Type'].replace('image/', '')
        results = re.match(pattern, image_type).string
        print(results)
        with open(path + '/{0}.{1}'.format(uuid.uuid4().hex, image_type), 'wb') as temp_file:
            temp_file.write(image.content)

        time.sleep(sleep)
