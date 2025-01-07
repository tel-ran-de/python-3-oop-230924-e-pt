# Импортировать библиотеку Re.
# Загрузить текст из файла live-coding/regex-1.txt.
# Найти в тексте название «Париж».
# Найти все слова на английском языке.
# Найти в тексте все имена на английском языке (с большой буквы).
# Найти все пустые строки.
# Найти все последовательности из двух или более заглавных букв.
# Найти все слова из двух или более заглавных букв.

import re


def main():
    # Загрузить текст из файла live-coding/regex-1.txt.
    with open('regex-1.txt', 'r') as file:
        text = file.read()

    print('Sample text:\n')
    print(text)
    print('* ' * 16)
    print('* ' * 3, end='')
    print(' ' * 3 + 'Solutions' + ' ' * 4 + '* ' * 5)
    print('* ' * 16)

    # Найти в тексте название «Париж».
    print('\nНайти в тексте название «Париж»:')
    match = re.findall('Пdsvfs', text)
    for n, m in enumerate(match):
        print(f'{n}: {m}')

    # Найти все слова на английском языке.
    print('\nНайти все слова на английском языке:')
    match = re.findall(r'\b[a-zA-Z]+\b', text)
    for n, m in enumerate(match):
        print(f'{n}: {m}')

    # Найти в тексте все имена на английском языке (с большой буквы)
    print('\nНайти все слова на английском языке (с большой буквы):')
    match = re.findall(r'\b[A-Z][a-z]*\b', text)
    for n, m in enumerate(match):
        print(f'{n}: {m}')

    # Найти все пустые строки
    print('\nНайти все пустые строки:')
    match = re.findall(r'^\s*$\n', text, re.MULTILINE)
    print(f'Пустых строк: {len(match)}')

    # Найти все последовательности из двух или более заглавных букв
    print('\nНайти все последовательности из двух или более заглавных букв:')
    match = re.findall(r'[A-Z,А-Я]{2,}', text, re.MULTILINE)
    print('Последовательности из двух или более заглавных букв:')
    for i, m in enumerate(match):
        print(f'{i}: {m}')

    # Найти все слова из двух или более заглавных букв
    print('\nНайти все слова из двух или более заглавных букв:')
    match = re.findall(r'\b[A-Z,А-Я]{2,}\b', text, re.MULTILINE)
    print('Cлова из двух или более заглавных букв:')
    for i, m in enumerate(match):
        print(f'{i}: {m}')


if __name__ == '__main__':
    main()
