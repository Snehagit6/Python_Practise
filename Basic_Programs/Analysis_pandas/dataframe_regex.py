import pandas as pd
import re

left = pd.DataFrame({
         'id':[78987,2890,3987,4098,5897],
         'Name': ['Alex', 'Amy', 'Allex', 'Alive', 'Ayoung'],
        'Date':['08/09/2014','08/10/2014','08/11/2014','08/12/2014','08/01/2015']})

right = pd.DataFrame(
         {'id':[78987,2890,3987,4098,5897],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'Date':['08/09/2013','08/10/2014','08/11/2014','09/11/2014','08/01/2015']})

print(left,'\n',right)


for d in left['Date']:
    print(d)