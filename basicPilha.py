class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def pull(self):
        if self.size == 0:
            raise Exception("Pilha Vazia")
        self.size -= 1
        return self.items.pop()

    def get_top(self):
        if self.size == 0:
            return False
        return self.items[-1]

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
