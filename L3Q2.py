from basicPilha import Stack


def invert():
    pil = Stack()
    exp = input("Digite a Expressão: ")
    for i in exp:
        pil.push(i)
    while True:
        if pil.is_empty():
            break
        elif pil.get_top().isdigit():
            a = pil.pull()
            if not pil.is_empty() and pil.get_top().isdigit():
                b = pil.pull()
                if not pil.is_empty() and pil.get_top().isdigit():
                    c = pil.pull()
                    if not pil.is_empty() and pil.get_top().isdigit():
                        d = pil.pull()
                        print("{}{}{}{}".format(d, c, b, a), end='')
                    else:
                        print("{}{}{}".format(c, b, a), end='')
                else:
                    print("{}{}".format(b, a), end='')
            else:
                print(a, end='')
        elif pil.get_top() == '(':
            pil.pull()
            print(')', end='')
        elif pil.get_top() == ')':
            pil.pull()
            print('(', end='')
        else:
            print(pil.pull(), end='')


if __name__ == "__main__":
    invert()
