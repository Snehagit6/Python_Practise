import re
s ='I8s the 3rd War'

#Meta characters
# \   Used to drop the special meaning of character
#     following it (discussed below)
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One ore more occurrences
# {}  Indicate number of occurrences of a preceding RE
#     to match.
# ()  Enclose a group of REs

x = re.match("^I8s.*War$",s)
if bool(x) == True:
    print("String \'%s\' has I8s at the first and War at the end"%s)
else:
    print("String \'%s\' doesnot have I8s at the first and War at the end"%s)

x=re.findall("a",s)
print(x)


#Splitting string with re
str1 = "I love my India"


x = re.split('\s',str1,2)#Third parameter is the maxsplit character.
print("Split string",x)
#Replacing string with other str
x = re.sub('\s','*',str1,2)
print(x)
# print(str.replace(' ','*'))
x = re.search(r'\bI\w+',str1)#Expression searches all words'w+' starting with 'I'
print(x.span())
print(x.string)
print(x.group())

#Function compile()
# Regular expressions are compiled into pattern objects, which
# have methods for various operations such as searching for pattern
# matches or performing string substitutions.

# \d   Matches any decimal digit, this is equivalent
#      to the set class [0-9].
#\d+   Matches any decimal digit, this is equivalent
        # to the set class [0-9].
# \D   Matches any non-digit character.
# \s   Matches any whitespace character.
# \S   Matches any non-whitespace character
# \w   Matches any alphanumeric character, this is
#      equivalent to the class [a-zA-Z0-9_].
# \W   Matches any non-alphanumeric character,viz.special characters

# Example
string1 = "This is Python* 123Regex"

print(re.compile('\W+').findall(string1))

z = re.compile('ab*')
print(z.findall("abbaabbab"))

# Function:split()

# Split string by the occurrences of a character or a pattern,
# upon finding that pattern, the remaining characters from the string
# are returned as part of the resulting list.

# re.split(pattern, string, maxsplit=0, flags=0)

string3 = "If the blackslash is to be used without its \n special meaning as metacharcter $, use '\\'"
print(re.split('I',string3,flags=re.IGNORECASE))


string4="Subject has Uber booked already"
print(re.sub('ub',"*",string4,flags=re.IGNORECASE))


strn="This is Python"
x=re.search("is",strn)
print(x.span())
print(x.group())
print(re.search("is",strn[x.span()[1]:]).span())
print(re.split('is',strn))

with open("G:\\Pythonautomation_softwares\\Sanfoundry_programs\\Regex_srch.txt",'r+') as fo:
    for f in fo:
        # x=re.findall("\S+@\S.\S+",f)
        #Regex for filtering out email
        x = re.findall("[\w.-]+@[\w.-]+\.com",f)
        # x=re.findall("^(\w+)@",f)
        if x:
            print(x)
            for i in x:
                print(i.replace('@','$'))
        m_n = re.findall("\d{10}",f)
        if m_n:
            print(m_n)


date = "12.07.2019"
print(re.findall("^(0[1-9]|1[0-9]|2[0-9]|3[0-1])([./-])(0[1-9]|1[0-2])([./-])(\d{2,4})+",date))
