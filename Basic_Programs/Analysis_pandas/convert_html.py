import pandas as pd
import os
from Basic_Programs.Analysis_pandas.write_tohtml import *
from Basic_Programs.Analysis_pandas.Web_scrapping import *
left =pd.DataFrame({
         'id':[78987,2890,3987,4098,5897],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right =pd.DataFrame(
         {'id':[78987,2890,3987,4098,5897],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['subject','sub2','sub3','sub6','sub5']})

g="j'g+='%d'%9'"
# list=[]
# for i in df.columns.tolist():
#     if "x" in i:
#         i=i.replace('x','source')
#
#     elif "y" in i:
#         i=i.replace('y','target')
#     list.append(i)
# df.columns=list
# print(df)

col_l=left.columns.tolist()
c=0
# new_list=[]
# for i in col_l:
#     i=str(i)+"_source"
#     col_l.append(i)
#Use zip() function
while c < len(right.columns.tolist()):
    for j,i in zip(right.columns.tolist(),left.columns.tolist()):
        val = right[j]
        col_i=col_l.index(i)
        ind=col_i+1
        if col_i!=0:
            ind=ind +c
        left.insert(loc=ind, column='{}_target'.format(i), value=val)

        c+=1
columns=[]
for l in left.columns.tolist():
    if "target" not in str(l):
        l=l.replace(str(l),str(l)+"_source")
        columns.append(l)
    else:
        columns.append(l)

left.columns=columns
left['Result']=""
for i in range(len(left.index.values.tolist())):
    l=0
    while(l <len(left.columns.tolist())-1):
        sv=left.loc[[i],left.columns[l]].tolist()
        tv=left.loc[[i],left.columns[l+1]].tolist()
        if str(sv) !=str(tv):
            left.loc[[i],'Result']='FAILED'
            break

        else:
          left.loc[[i], 'Result'] = 'PASSED'
        l+=2



#

# print(left)

# left.to_html(os.getcwd()+"\\appendhtml.html")
#
# end=time()
# elapsed=end-start
#Use decorator function!!
modify_result_report(write_to_html_file(left, title='Dummy_Scenario', filename=("G:\\Pythonautomation_softwares\\Sanfoundry_programs\\Basic_Programs\\Analysis_pandas\\appendhtml.html")))