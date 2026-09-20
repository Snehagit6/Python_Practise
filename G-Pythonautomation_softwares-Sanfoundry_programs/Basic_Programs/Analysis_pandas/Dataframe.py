import numpy
from pandas import Series,DataFrame
import pandas as pd
from pandas.io.json.normalize import _convert_to_line_delimits
#
# # data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# # df = pd.DataFrame(data)
# # print(df)
#
# list1=['Akash', 'Vikash', 'Manash']
# list2=[12, 67, 43]
# df1 = pd.DataFrame({'A':list1, 'B':list2})#DataFrame constructor is being called
# df1.index=['row'+str(i)for i in range(0,3)]
# # print(df1)
# list3=['Df','Akash','Manash']
# df2 = pd.DataFrame({'A':list1, 'B':list3})
# df2.index=['row'+str(i)for i in range(0,3)]
# d=df2.to_dict()
# c=list(d.keys())
# i=list((list(d.values())[0]).keys())
# df3=pd.DataFrame(list(d.values()),columns=c,index=i)
# print(df3)

# l=(df2).iloc[:,1].tolist()
# print(l)
# print([i for i,j in zip(list1,l) if i.lower()!=j.lower()])

# G:\\Pythonexceldata 'Data'
# pd.read_excel("G:\\Pythonexceldata.xlsx",sheet_name='Data')
# print(pd)


# csv_data=pd.read_csv("C:\\Users\\hp\\Desktop\\Hobby_name_age.csv")
# print(csv_data)
# d={'NAME':pd.Series(['Ankit','Sachit','Rohan']),'AGE':pd.Series([10,20,10]),'HOBBY':pd.Series(['Cricket','Badminton','Tennis'])}
# pd.DataFrame(d).to_csv("C:\\Users\\hp\\Desktop\\Hobby_name_age.csv",index=False)


#Copying contents
# import webbrowser
# website="https://www.bseindia.com/"
# webbrowser.open_new_tab(website)
df2=pd.read_clipboard()
print(df2)
