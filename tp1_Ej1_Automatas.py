def validate_string(string):

    has_alphanumeric = any(char.isalnum() for char in string)

    has_letter = any(char.isalpha() for char in string)

    has_uppercase = any(char.isupper() for char in string)

    has_lowercase = any(char.islower() for char in string)

    has_digit = any(char.isdigit() for char in string)

    has_length = len(string) >= 8

    return has_alphanumeric, has_letter, has_uppercase, has_lowercase, has_digit, has_length


code = validate_string("xYz8")
code1 = validate_string("xy@z!")
print(code)
print(code1)
