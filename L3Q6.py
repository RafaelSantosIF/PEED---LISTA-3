from basicPilha import Stack


def is_balanced(exp):
    pil = Stack()
    for char in exp:
        if char == '(':
            pil.push(char)
        elif char == ')':
            if pil.is_empty() or pil.get_top() != '(':
                return False
            else:
                pil.pull()

        if char == '[':
            pil.push(char)
        elif char == ']':
            if pil.is_empty() or pil.get_top() != '[':
                return False
            else:
                pil.pull()

        if char == '{':
            pil.push(char)
        elif char == '}':
            if pil.is_empty() or pil.get_top() != '{':
                return False
            else:
                pil.pull()

    if pil.is_empty():
        return True
    else:
        return False

def main():
    exp = input("Digite a Expressão: ")
    if is_balanced(exp):
        print("Balanceado")
    else:
        print("Desbalanceado")

if __name__ == "__main__":
    main()
