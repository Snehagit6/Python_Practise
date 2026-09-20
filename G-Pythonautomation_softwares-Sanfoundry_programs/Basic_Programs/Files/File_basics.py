# #file_obj=open(file_name[,access mode][,buffering])
# #access mode[default]:'r'
# #buffering->No. of bytes flushed to the file:default:System's buffer size .r


fo=open('.\Associates_1.csv')
print("File open"
        "ed successfully")
# content=fo.read()# read() reads total no. of bytes from the file
# print("Bytes \n",content)
# for i in fo:
#     print(i)
# content=(fo.readline())#readline captures single line at a time returns a string
# print("String ",content)

content=(fo.readlines())
content=[line.strip('\n') for line in content]
content=[line.split(';') for line in content]
header=content.pop(0)
content=[dict(zip(header,record)) for record in content]
print(content)
print([i['Location'] for i in content if i['EmployeId']=='976780'])

fo.close()

#readlines captures all elements in a list
# print(().join(content))

#Processing data from the text file into a dictionary
# import re
# try:
#     fp=open("C:\\Users\\hp\\Desktop\\Hobby_name_age.txt")
#     contents=fp.readlines()
#     conts=[re.split('\n|;',c)for c in contents]
#     for ele in conts:
#         if '' in ele:
#             ele.remove('')
#     # conts=[c.split('\n') for c in contents]
#     # conts=[c.split(';') for c in cont ents]
#     header=conts.pop(0)
#     conts=[dict(zip(header,c))for c in conts]
#     print(conts)
#     print(conts[0]['NAME'])
# 
# except FileNotFoundError as fe:
#     print(fe.args)

# count the number of words in the file
# num_words=0
# with open("C:\\Users\\hp\\Desktop\\Hobby_name_age.txt") as fo:
#     for line in fo:
#         words=line.split()
#         num_words+=len(words)
# print("Number of words:",num_words)
#