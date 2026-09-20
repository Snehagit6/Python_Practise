import sys

class Stack:
    """Python program to check whether a string is a palindrome using a stack."""
    def __init__(self):
        self.items = []

    def _is_empty(self):
        return True if not self.items else False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self._is_empty() else sys.exit("No item present")


s = Stack()
text = input("Please enter string")

for each in text:
    s.push(each)

if text == "".join([s.pop() for _ in range(len(s.items))]):
    print(f"String: {text} is palindrome")
else:
    print(f"String: {text} is not palindrome")