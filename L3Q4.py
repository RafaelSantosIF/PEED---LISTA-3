from basicPilha import Stack


def conv_BinToDec(num):
    pil = Stack()
    n = num
    while num > 0:
        res = num % 2
        n = n//2
        pil.push(res)
    return pil

def main():
    dec = int(input("Número Decimal: "))
    result = conv_BinToDec(dec)

    while not result.is_empty():
        print(result.pull())

if __name__ == "__main__":
    main()