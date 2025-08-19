class Stack:
    def __init__ (self):
        self.items = []
    def is_empty (self):
        return len(self.items) == 0
    def push (self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self.items)
Stack = Stack()
Stack.push(1)
Stack.push(2)
Stack.push(3)
print (Stack.pop())
print(Stack.peek())
print(Stack.size())

