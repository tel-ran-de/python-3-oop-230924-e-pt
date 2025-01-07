# Импортировать библиотеку Re.
# Загрузить текст из файла live-coding/regex-2.txt.
# Найти все телефонные номера в формате (123) 456-7890 или 123-456-7890.
# Найти все даты в формате DD/MM/YYYY или DD-MM-YYYY.
# Найти все email-адреса.
# Найти все email-адреса, содержащие символ подчеркивания.
# Найти все слова, содержащие не менее одной цифры.

import re


def print_match(pattern: str, find_str: str, key=re.MULTILINE):
    match = re.findall(pattern, find_str, key)
    for n, m in enumerate(match):
        print(f'{n}: {m}')
    print('* ' * 20)
    print('\n')

def main():
    # Загрузить текст из файла live-coding/regex-2.txt.
    with open('regex-2.txt', 'r') as file:
        text = file.read()
    print(text, '\n')

    # Найти все телефонные номера в формате (123) 456-7890
    print('Найти все телефонные номера в формате (123) 456-7890 или 123-456-7890:')
    print_match(r'\D\d{3}\D{1,2}\d{3}-\d{4}', text)

    # Найти все даты в формате DD/MM/YYYY или DD-MM-YYYY.
    print('Найти все даты в формате DD/MM/YYYY или DD-MM-YYYY:')
    print_match(r'\b\d{2}[/|-]\d{2}[/|-]\d{4}\b', text)

    # Найти все email-адреса.
    print('Найти все email-адреса:')
    print_match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

    # Найти все email-адреса, содержащие символ подчеркивания.
    print('Найти все email-адреса, содержащие символ подчеркивания:')
    print_match(r'\b[A-Za-z0-9._%+-]+_[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

    # Найти все слова, содержащие не менее одной цифры.
    print('Найти все слова, содержащие не менее одной цифры:')
    print_match(r'\b(?=\w*\d)(?=\w*[A-Za-z])\w+\b', text)


if __name__ == '__main__':
    main()
