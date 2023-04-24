import re


def validator_email(emails):
    email_regex = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.(com|net|es|org|biz)(\.(ar|br|uk|mx|ur))?$'
    emails = [emails]

    for email in emails:
        if re.match(email_regex, email):
            print(f'{email} is a correct email')
        else:
            print(f'{email} not a correct email')


def validator_url(url):
    url_regex = r'^(HTTP://|HTTPS://|http://|https://)|(www)+\.[a-zA-Z0-9]+\.(com|net|es|org|biz)(\.(ar|br|uk|mx|ur))?$'
    url = [url]

    for urls in url:
        if re.match(url_regex, urls):
            print(f'{urls} is a correct URL')
        else:
            print(f'{urls} not a correct URL')


email = str(input('Enter your email: '))
validator_email(email)


url = str(input('Enter your URL: '))
validator_url(url)
