# Найдите в тексте все имена. Именно имена в человеческом восприятии.
# Используйте библиотеку NER для лемматизации и синтаксического разбора текста.

# http://docs.deeppavlov.ai/en/master/features/models/NER.html#2.-Get-started-with-the-model

# pip install deeppavlov
# python -m deeppavlov install ner_ontonotes_bert

from deeppavlov import build_model


def main():
    with open('regex-2.txt', 'r') as file:
        text = file.read()

    ner_model = build_model('ner_ontonotes_bert', download=True, install=True)

    tokens, tags = ner_model([text])
    for i, tag in enumerate(tags[0]):
        if (tag == 'B-PERSON') or (tag == 'I-PERSON'):
            print(tokens[0][i], tag)


if __name__ == '__main__':
    main()
