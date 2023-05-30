def is_balanced(exp):
    p = []
    for char in exp:
        if char == '(':
            p.append(char)
        elif char == ')':
            if not bool(p) or p[-1] != '(':
                return False
            else:
                p.pop()

    if not bool(p):
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