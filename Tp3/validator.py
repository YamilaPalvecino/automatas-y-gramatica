import re
from constants import *


def validator_email(emails):
    email_regex = EMAIL_REGEX
    if re.match(email_regex, emails):
        print(f'{emails}', EMAIL_CORRECT)
    else:
        print(f'{emails}', EMAIL_INCORRECT)


def validator_url(url):
    url_regex = URL_REGEX
    if re.match(url_regex, url):
        print(f'{url}', URL_CORRECT)
    else:
        print(f'{url}', URL_INCORRECT)

def validator_IPV4(line):
    if re.fullmatch('((25[0-5]|000|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$', line):
        print(f'{line}',IP_CORRECT)
    else:
        print(f'{line}',IP_INCORRECT)


def lexical_Analyzer(file):
    with open(f'{file}.txt', 'r') as file_text:
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
