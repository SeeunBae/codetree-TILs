class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    
    def size(self):
        return len(self.items)

    def empty(self):
        return not self.items

    def top(self):
        if self.empty():
            raise Exception ("Stack is empty")
        return self.items[-1]



n=int(input())
s=Stack()
for _ in range(n):
    command=input()

    if command.startswith("push"):
        x=int(command.split()[1])
        s.push(x)
    elif command=="size":
        print(s.size())
    elif command=="empty":
        print(1 if s.empty() else 0)
    elif command=="pop":
        print(s.pop())
    else:
        print(s.top())