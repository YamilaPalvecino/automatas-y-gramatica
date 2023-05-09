from validator import *
from constants import *


def menuValidator():
    b = True
    while b:
        print(MENU)
        select = str(input(SELECT_OPTION))

        if select == '1':
            email = str(input(ENTER_MAIL))
            validatorEmail(email)

        elif select == '2':
            url = input(ENTER_URL).strip()
            validatorURL(url)

        else:
            print(INCORRECT_CHOICE)


menuValidator()
