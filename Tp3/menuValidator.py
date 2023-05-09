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

        elif select == '3':
            ipv4 = input(ENTER_IP).strip()
            validatorIPV4(ipv4)

        elif select == '4':
            #file = str(input(ENTER_TEXT))
            file = r"C:\Users\EMANUEL\Documents\texto"
            lexicalAnalyzer(file)

        elif select == '5':
            quit()

        else:
            print(INCORRECT_CHOICE)


menuValidator()
