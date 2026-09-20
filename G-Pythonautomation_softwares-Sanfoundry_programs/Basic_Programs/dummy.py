#
# dict1 = {0: 'Zara',1:'Sara'}
# #    , 1: 7}
# # dict2 = {0: 7,
# dict2= {0: 'Tara',1:'Sara'}
# print(dict1.values())
# print(dict2.values())
# l=[i for i in dict1.values() if i not in dict2.values()]
# l2=[j for j in dict2.values()if j not in dict1.values()]
# print((f"{l} != {l2}"))
#
#
# from Basic_Programs.Database.Reading_tables import col_count
#
# h='<tr><th></th><td></td></tr>\n'*4
# r=h.replace('<td></td>','<td></td>'*col_count())
# print(r)

s='dogs'
s_=list(s)
i=1
permutation_=[]
def permutation(l):
    # for each in range(len(l)):
        # while(i<=6):

                    permutation_.append(''.join(s_))
                    for k in range(1,len(l)-1):

                        l[k],l[k+1]=l[k+1],l[k]

                        permutation_.append(''.join(l))


for i in range(len(s_)):

    s_[0], s_[i] = s_[i], s_[0]

    permutation(s_)
    permutation([s_[0]]+s_[-1:0:-1])

print(permutation_,len(permutation_))
# print([s_[0]]+s_[-1:0:-1])
# def get_html_tbl(seq, col_count):
#     if len(seq) % col_count:
#         seq.extend([''] * (col_count - len(seq) % col_count))
#     tbl_template = '<table>%s</table>' % ('<tr>%s</tr>' % ('<td>%s</td>' * col_count) * (len(seq)/col_count))
#     return tbl_template % tuple(seq)
#
# import math   # This will import math module
#
# print ("math.log10(2.01103e+07) : ", round(math.log10(2.01103e+07),4))
# print ("math.log10(20110311) : ", round(math.log10(20110311),4))
#
#
# x=2.01103e+07
#
# print('%E'%x)
# for i in str(x):
#     print(i)
# x=str(x)[(str(x).index('.')+1):str(x).index('e')]
# l=len(x)
# print(x)
# y=20110311
# # print(str(int(x)))
# print(f'%.{l}E'%y)