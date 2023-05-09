import re
from constants import *


def validatorEmail(emails):
    if re.fullmatch(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.(com|net|es|org|biz)(\.(ar|br|uk|mx|ur))?$', emails):
        print(f'{emails}', EMAIL_CORRECT)
    else:
        print(f'{emails}', EMAIL_INCORRECT)


def validatorURL(url):
    if re.fullmatch('(https://|http://)?(www\.)?[A-Za-z0-9_-]+\.[a-zA-Z]{3}(\.[A-Za-z]{2})?(/[A-Za-z0-9_-]+)*(\.(php|html))?(\?([A-Za-z]+=[A-Za-z0-9]+&?)*)?', url):
        print(f'{url}', URL_CORRECT)
    else:
        print(f'{url}', URL_INCORRECT)