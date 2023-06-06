from basicPilha import Stack


def conv_BinToOct(num):
    pil = Stack()
    n = num
    while num > 0:
        res = num % 8
        n = n//8
        pil.push(res)
    return pil

def main():
    dec = int(input("Número Decimal: "))
    result = conv_BinToOct(dec)

    while not result.is_empty():
        print(result.pull())

if __name__ == "__main__":
    main()