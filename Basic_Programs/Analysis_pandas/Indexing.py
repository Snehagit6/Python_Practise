import pandas as pd
import numpy as np
import datetime
#Indexing the Dataframe of random numbers as per the row number.
def row_no_index():
    df=pd.DataFrame(pd.np.random.random(100))
    df.index=['row_'+str(i)for i in range(1,101)]
    print(df.sample(frac=0.7))#Printing 70% of data
    print(df.shape)

#Indexing the dataframe of dates as per a specific format
def date_format_index():
    df=pd.DataFrame(pd.to_datetime(['20150720','20161028'],format='%Y%m%d'))
    df.index=['d1','d2']
    print(df.to_dict())
    print(df)
    
def datetime_dataframe():
    df=pd.DataFrame({'year':[2014,2015],'month':[7,2],'day':[28,16]})
    print(df)

# bdate_range,date_range
def date_range():
    date_set=pd.date_range('1-Sep-2017 ','15-Sep-2017',freq='D')
    df=pd.DataFrame(date_set)
    df.index=['dates' for i in date_set]
    print(df) 
def date_range_ops():
    d = pd.date_range('11-Sep-2017', '17-Sep-2017', freq='2D')
    print(len(d[d.isin(pd.to_datetime(['12-09-2017', '15-09-2017']))]))

    d=pd.date_range('11-Sep-2017', '17-Sep-2017', freq='2D')
    print(d)
  
    d=pd.period_range('11-Sep-2017', '17-Sep-2017', freq='M')
    print(d)
    d=pd.bdate_range('11-Sep-2017','17-Sep-2017',freq='2D')
    
def format_date():
    df = pd.DataFrame({'Closed Date':['05/01/2016 05:10:10 AM', 
                                  '05/01/2016 05:10:10 AM', 
                                   np.nan]})

    col='Closed Date'
    df[col] = pd.to_datetime(df[col], format='%m/%d/%Y %I:%M:%S %p')
    print (df)
    
# row_no_index()
# date_format_index()
# datetime_dataframe()
# date_range()
date_range_ops()