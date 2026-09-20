
# z = np.arange(10, 16)
# 
# s = pd.Series(z, index=list('abcdef'))
# print(s)
# print(s[1:4])
# df=pd.DataFrame(pd.read_excel("G:\\Pythonexceldata.xlsx"))
# print(df.loc[0])


# df=pd.read_table("C:\\Users\\hp\Desktop\\Dropbox.pdf")
# print(df)

# from tabula import read_pdf
# df = read_pdf("C:\\Users\\hp\Desktop\\Dropbox.pdf")
# print(df)

import pandas as pd

import numpy as np

from pandas import Series,DataFrame

obj = Series([8,4,5,'g'])
print(obj,'\n',obj.values,'\n',obj.index)

case1 = Series([1000,2000,3000],index=['Germany','Australia','Britain'])
print(case1)

print(case1[case1>1000])
case2 = case1.to_dict()
countries = ['Germany','Australia','Britain','Greenland']
case2 = Series(case2,index=countries)
print(pd.isnull(case2))
print(case1+case2)