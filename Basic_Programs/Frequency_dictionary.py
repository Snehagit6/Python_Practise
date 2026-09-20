from collections import Counter
words = ['Sneha','Rubai','Sneha','Rimi']
word_frequency = {w:words.count(w)for w in words}
print(word_frequency)
#To find frequency of a word with certain value
word_frequency = {w:words.count(w)for w in words if words.count(w)>1}
print(word_frequency)

str = "Sneha"
print(dict(Counter(str)))

name = "harish"
namelist = []
for n in name:
    namelist.append(n)
print([namelist.count(n) for n in namelist])