from basicPilha import Stack


def is_palindrome(word):
    pilWord = Stack()
    pilPalindrome = Stack()
    for character in word:
        pilWord.push(character)
    for character in range(len(word)):
        pilPalindrome.push(pilWord.pull())
    palindrome = pilPalindrome.to_text()
    if palindrome == word:
        return True
    else:
        return False

def main():
    word = input("Palavra: ")
    if is_palindrome(word):
        print("É um Palíndromo!")
    else:
        print("Não é um Palíndromo!")

if __name__ == "__main__":
    main()