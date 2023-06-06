from basicPilha import Stack


def conv_BinToHex(decimal):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    pil = Stack()

    while decimal > 0:
        res = decimal % 16
        pil.push(conversion_table[res])
        decimal = decimal // 16
    return pil

def main():
    dec = int(input("Número Decimal: "))
    result = conv_BinToHex(dec)

    while not result.is_empty():
        print(result.pull(), end='')

if __name__ == "__main__":
    main()
