from functools import reduce

def solve(string):

    tokens = string.split("+")
    sum = 0
    producto = 1

    #operación multiplicación
    for element in tokens:
        if "*" in element:
            multi_str = element.split('*')
            multi_int = [int(numero) for numero in multi_str]
            producto = reduce(lambda x, y: x * y, multi_int)
            tokens.remove(element)

    tokens = [int(num) for num in tokens]
    tokens.append(producto)

    #operación suma
    for num in tokens:
        sum += num

    return sum


    #return resultado


operation = str(input("Enter your value: "))
print(solve(operation))
