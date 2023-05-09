import re
from constants import *


def validator_Email(emails):
    if re.fullmatch(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.(com|net|es|org|biz)(\.(ar|br|uk|mx|ur))?$', emails):
        print(f'{emails}', EMAIL_CORRECT)
    else:
        print(f'{emails}', EMAIL_INCORRECT)


def validator_URL(url):
    if re.fullmatch('(https://|http://)?(www\.)?[A-Za-z0-9_-]+\.[a-zA-Z]{3}(\.[A-Za-z]{2})?(/[A-Za-z0-9_-]+)*(\.(php|html))?(\?([A-Za-z]+=[A-Za-z0-9]+&?)*)?', url):
        print(f'{url}', URL_CORRECT)
    else:
        print(f'{url}', URL_INCORRECT)


def validator_IPV4(line):
    if re.fullmatch('((25[0-5]|000|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$', line):
        print(f'{line}', IP_CORRECT)
    else:
        print(f'{line}', IP_INCORRECT)


def lexical_Analyzer(file):
    with open(f'{file}.txt', 'r', encoding="utf-8") as file_text:
        text = file_text.read()
        words = re.findall(r'\w+', text.lower())
        word_frequency = {}
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        most_frequent_word = max(word_frequency, key=word_frequency.get)
        print(TEXT_COUNT_MSG, f'{len(words)}', TEXT_CONTENT)
        print(WORD_REPEATED_MSG, f'{most_frequent_word}', CONTENT_REPEATED_WORD,
              f'{word_frequency[most_frequent_word]}')

