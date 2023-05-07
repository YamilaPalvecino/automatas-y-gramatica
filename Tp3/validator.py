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
