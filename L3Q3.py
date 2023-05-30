from basicPilha import Stack


def infix_to_postfix(exp):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operates = Stack()
    postfix = []
    numbers = '0123456789'
    for character in exp:
        if character in numbers:
            postfix.append(character)
        elif character == '(':
            operates.push(character)
        elif character == ')':
            while operates.get_top() != '(':
                postfix.append(operates.pull())
            operates.pull()
        elif character in precedence:
            while not operates.is_empty() \
                    and operates.get_top() != '(' \
                    and precedence[character] <= precedence[operates.get_top()]:
                postfix.append(operates.pull())
            operates.push(character)
    while not operates.is_empty():
        postfix.append(operates.pull())
    return ''.join(postfix)

def calc_postfix(exp):
    numbers = '0123456789'
    valfirst = 0
    valsecond = 0
    result = 0
    for character in exp:
        if character in numbers and valfirst == 0:
            valone = int(character)
            valfirst = 1
        elif character in numbers and valsecond == 0:
            valtwo = int(character)
            valsecond = 1
        if character == '+':
            result = (valone + valtwo)
            valone = result
            valsecond = 0
        elif character == '-':
            result = (valone - valtwo)
            valone = result
            valsecond = 0
        elif character == '*':
            result = (valone * valtwo)
            valone = result
            valsecond = 0
        elif character == '/':
            result = (valone / valtwo)
            valone = result
            valsecond = 0

    return result




def main():
    exp = input("Digite a Expressão: ")
    exp = infix_to_postfix(exp)
    print(exp)
    print("Resultado {}".format(calc_postfix(exp)))


if __name__ == "__main__":
    main()