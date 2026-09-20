#The most occurring number in a string using Regex in python
import re
string = "geek55of55geeks4abc3dr2"
num_l = re.findall("\d+",string)
count_l = [num_l.count(each) for each in num_l]
count_l = lambda each:num_l.count('m')
print(count_l)

#Generator :In memory
# range(6)
# xrange

# max = max(count_l)
# for each in num_l:
#     if num_l.count(each) == max:
#         print(each)
#         break
#
#
# l = []
# s = "IamVeryIntense"
# re.findall('[A-Z][a-z]*', s)
# for each in re.findall('[A-Z][a-z]*', s):
#     l.append(chr(ord(each[0])+32)+l[1:])
