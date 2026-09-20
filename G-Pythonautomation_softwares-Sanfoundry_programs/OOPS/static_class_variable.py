class CSStudent:
    stream = 'cse'  # Class Variable or Static variable
    def change(self):
        stream = CSStudent.stream * 2
    def __init__(self, name, roll):
    # ,stream):
        self.change()
        self.name = name  # Instance Variable
        self.roll = roll  # Instance Variable
        # self.stream=stream

# Objects of CSStudent OOPS
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)
a.change()
print(a.stream)  # prints "cse" ## Class Variable or Static variable can be shared by all the instances of the OOPS
print(b.stream)  # prints "cse"
print(a.name)  # prints "Geek"
print(b.name)  # prints "Nerd"
print(a.roll)  # prints "1"
print(b.roll)  # prints "2"

# Class variables can be accessed using OOPS
# name also
print(CSStudent.stream)