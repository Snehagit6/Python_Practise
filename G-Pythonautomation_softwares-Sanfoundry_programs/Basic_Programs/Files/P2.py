#Python Program to Count the Number of Words in a Text File

# print(len(f.read().split('\n')[:-1]))
num_words=0
num_lines=0
num_letter=0
# print(sum([len(each)for each in [each.split(' ') for each in f.read().split('\n')[:-1]]]))
try:
    with open("./File_read.txt",'r+') as f:
        for each in f:
            num_lines+=1
            words=each.split()
            num_words+=len(words)
            for each in words:
                for letter in each:
                    num_letter+=1
        print("=" * 23, file=f)
    #Printing to the file in the next line

    print("Number of lines:{lines} ,words:{words},letters :{letters} in file".format(lines=num_lines,words=num_words,\
                                                                                     letters=num_letter))
except FileNotFoundError as e:
  print("Exception",e.args)

