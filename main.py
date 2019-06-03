import utils


def main():
    url = input('Вставь ссылку на тред ')
    photo_limit = input('Задай ограничение на количество, если нужно ')
    source = utils.get_page(url)

    if photo_limit.isdigit():
        links = utils.parse_page(source, int(photo_limit))
    else:
        links = utils.parse_page(source)

    utils.dl_image(links)

if __name__ == '__main__':
    main()


# TODO: Убрать константу пути загрузки, путь должен определяться в run-time
