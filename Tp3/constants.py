
#constants Menu Validator

MENU = "1 - Validate Mail\n"\
       "2 - Validate URL\n"\
       "3 - Validate IPV4\n"\
       "4 - Analyze text\n"\
       "5 - Exit"
SELECT_OPTION = "Enter Option N°: "

ENTER_MAIL = 'Enter your email: '
ENTER_URL = 'Enter your URL: '
ENTER_IP = 'Enter your IPV4 (example: 192.108.255.255): '
INCORRECT_CHOICE = 'Incorrect choice'
ENTER_TEXT = 'Enter the route of your text document: '

#constas validator
EMAIL_REGEX = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.(com|net|es|org|biz)(\.(ar|br|uk|mx|ur))?$'
EMAIL_CORRECT = 'is a correct email'
EMAIL_INCORRECT = 'not a correct email'

URL_REGEX = r'^(HTTP://|HTTPS://|http://|https://)|(www)+\.[a-zA-Z0-9]+\.(com|net|es|org|biz)|(\.(ar|br|uk|mx|ur))?$'
URL_CORRECT = 'is a correct URL'
URL_INCORRECT = 'not a correct URL'

IPV4_REGEX = r'^(\d{1,3}\.){3}\d{1,3}$'
IP_CORRECT = 'The IP address is valid.'
IP_INCORRECT = 'The IP address is invalid.'
TEXT_COUNT_MSG = 'The text has '
TEXT_CONTENT = 'words'
WORD_REPEATED_MSG = 'The most repeated word is "'
CONTENT_REPEATED_WORD = '" number of times it is repeated'
NOMBRE_ARCHIVO = 'ipv4s.txt'
PATRON = '((25[0-5]|000|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$'