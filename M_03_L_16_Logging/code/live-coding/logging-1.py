import logging


def main():
    logger = logging.getLogger(__name__)

    # logging.basicConfig(level=logging.ERROR)

    logger.debug('This is DEBUG level message')
    logger.info('This is INFO level message')
    logger.warning('This is WARNING level message')
    logger.error('This is ERROR level message')
    logger.critical('This is CRITICAL level message')
    other_func()


def other_func():
    logger = logging.getLogger(other_func.__name__)
    logger.info(f'This is INFO level message from {other_func.__name__}')


if __name__ == '__main__':
    main()
