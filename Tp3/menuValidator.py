from validator import *
from constants import *


def menuValidator():
    b = True
    while b:
        print(MENU)
        select = str(input(SELECT_OPTION))

        if select == '1':
            email = str(input(ENTER_MAIL))
            validator_Email(email)

        elif select == '2':
            url = input(ENTER_URL).strip()
            validator_URL(url)

        elif select == '3':
            ipv4 = input(ENTER_IP)
            validator_IPV4(ipv4)

        elif select == '4':
            file = input(ENTER_TEXT)
            lexical_Analyzer(file)

        else:
            print(INCORRECT_CHOICE)


menuValidator()
