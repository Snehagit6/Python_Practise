import os
from subprocess import call
file = "D:\\Python_Practise_Programs\\Praccy_Progs\\" \
       "Basic_Programs\\Files\\Associates_2.csv"

#Reverse content of a file using Stack DS
class Stack():

    def __init__(self):

        self._arr = []

    def push(self, val):
        self._arr.append(val)

    def pop(self):
        if not self._arr:
            return "Stack is empty"
        return self._arr.pop()


def reverse_file(file):

    s = Stack()
    try:
        with open(file,"+r") as f:
            for line in f:
                s.push(line.rstrip("\n"))
        arr_len = len(s._arr)
        with open(file,"w+") as f:
            for i in range(arr_len):
                f.write(s.pop()+"\n")

    except FileNotFoundError as e:
        print("File Not Found")

    else:
        print("Written to file in reverse order")

# reverse_file(file)
# os.startfile(file)

def reverse_word(file):

    file_rev = file.replace("_2", "_rev")
    rev_line = []
    try:
        with open(file, "r+") as f:
            for line in f:
                rev_line.append(line[::-1].lstrip("\n")+"\n")
    except FileNotFoundError as e:
        print("Error : %s"%str(e.args))

    try:
        with open(file_rev, "w") as f:
            f.writelines(rev_line)
    except:
        print("Error in file writing")
    else:
        print("Written to file")

# reverse_word(file)

#Get number of characters, words, spaces and lines in a file
char_c, l_c, w_c, sp_c = 0,0,0,0
with open(file, "r+") as fo:
    for line in fo:
        print(line)
        l_c+= 1
        for word in line.rstrip("\n"):
            if word.isspace():
                print(word)
                sp_c+=1
            else:
                print(word)
                w_c+=1
            for l in word:
                print(l)
                if not l.isspace():
                    char_c+=1
print(char_c, l_c, w_c, sp_c)



