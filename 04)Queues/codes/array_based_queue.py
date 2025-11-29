class Queue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [None] * max_size
        self.size = 0
        self.front_index = 0
    
    def __len__(self):
        return self.size 
    
    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is Empty!")
        return self.Q[self.front_index]
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is Empty!")
        answer = self.Q[self.front_index]
        self.Q[self.front_index] = None 
        self.size -= 1
        self.front_index = (self.front_index + 1) % (self.max_size)
        return answer 
    
    def enqueue(self, item):
        if self.size == self.max_size:
            raise Exception("Queue overflow.")
        self.Q[(self.front_index + self.size) % self.max_size] = item 
        self.size += 1 

    def __str__(self):
        if self.is_empty():
            return "Queue: []\nInternal Array: " + str(self.Q)
        logical = []
        index = self.front_index
        for _ in range(self.size):
            logical.append(self.Q[index])
            index = (index + 1) % self.max_size
        return ("Queue (logical order): [" + ", ".join(str(x) for x in logical) + "]\n"
                "Internal Array: " + str(self.Q))
    
