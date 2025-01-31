class Stack:
    def __init__(self, size):
        self.size = size
        self.items = []

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            print("Ngăn xếp đã đầy")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Ngăn xếp rỗng")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

stack = Stack(6)
print(stack.is_empty()) 
stack.push(2.1)
print(stack.is_empty()) 
stack.push(3.9)
print(stack.pop())  
print(stack.pop()) 
print(stack.is_full()) 