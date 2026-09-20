import pandas as pd
df = pd.DataFrame({'A':[34, 78, 54], 'B':[12, 67, 49]}, index=['r1', 'r2', 'r3'])
# df.loc['r4']=[67,78]
# print(df[df.B>45])
print(df.loc['r2':'r3'])

# s = pd.Series([89.2, 76.4, 98.2, 75.9], index=list('abcd'))
# print(s[['c', 'a']])


