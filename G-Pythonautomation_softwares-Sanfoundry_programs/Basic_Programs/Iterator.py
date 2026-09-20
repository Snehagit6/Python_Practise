from itertools import groupby
n = [10, 13, 16, 22, 9, 4 , 37]
print([(group)for key,group in groupby(n)])