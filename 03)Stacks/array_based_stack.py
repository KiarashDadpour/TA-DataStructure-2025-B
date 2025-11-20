class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.S = [None] * self.max_size
        self.top = -1    

    def push(self, value):
        if self.top >= self.max_size - 1:
            raise Exception("Stack Overflow")
        self.top += 1
        self.S[self.top] = value

    def pop(self):
        if self.top == -1:
            raise Exception("Empty Stack !!!")
        item = self.S[self.top]
        self.S[self.top] = None
        self.top -= 1
        return item

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def get_top(self):   
        if self.top == -1:
            return None
        return self.S[self.top]

    def size(self):
        return self.top + 1

    def __str__(self):
        s = ""
        count = self.top
        while count >= 0:
            s += str(self.S[count]) + " "
            count -= 1
        return s
