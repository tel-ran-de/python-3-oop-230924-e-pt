import logging


def main():
    # создать логгер
    logger = logging.getLogger(__name__)

    # задать форматтеры
    stdout_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    file_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

    # создать потоки вывода логов
    stdout_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename=f'{__name__}.log', mode='w')

    # подключить к потокам форматтеры
    stdout_handler.setFormatter(fmt=stdout_formatter)
    file_handler.setFormatter(fmt=file_formatter)

    # добавить потоки вывода к логгеру
    logger.addHandler(hdlr=stdout_handler)
    logger.addHandler(hdlr=file_handler)

    # установить уровень логирования
    logger.setLevel(level=logging.DEBUG)

    logger.debug('This is DEBUG level message')
    logger.info('This is INFO level message')
    logger.warning('This is WARNING level message')
    logger.error('This is ERROR level message')
    logger.critical('This is CRITICAL level message')


if __name__ == '__main__':
    main()
