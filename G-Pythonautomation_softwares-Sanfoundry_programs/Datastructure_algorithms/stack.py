class Stack():
    """LIFO: Last In First Out"""
    def __init__(self, limit:int = 10):
        self.stack = []
        self.limit = limit

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, item):
        if len(self.stack)>=self.limit:
            return False
        self.stack.append(item)

    def pop(self):
        if not self.stack or not self.stack[-1]:
            return "Stack is empty"
        self.stack.pop()


stack = Stack(10)

for i in range(15):

    if stack.push(i) == False:

        print("Stack is full!")
        break
print(stack)

#Stack implementation of reversing a word
s = "sneha"
# l =list(s)
# rl = [l.pop() for item in range(len(s))]
# print(''.join(rl))