from validator import *
from constants import *


def menuValidator():
    b = True
    while b:
        print(MENU)
        select = str(input(SELECT_OPTION))

        if select == '1':
            email = str(input(ENTER_MAIL))
            validator_email(email)

        elif select == '2':
            url = str(input(ENTER_URL))
            validator_url(url)

        elif select == '3':
            validator_IPV4()

        elif select == '4':
            lexical_Analyzer()

        elif select == '5':
            quit()

        else:
            print(INCORRECT_CHOICE)


menuValidator()
