import numpy
from pandas import Series,DataFrame
import pandas as pd
from pandas.io.json.normalize import _convert_to_line_delimits
import os
from Basic_Programs.Analysis_pandas.write_tohtml  import *
# data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# df = pd.DataFrame(data)
# print(df)


df1 = pd.DataFrame([[1,2,'k'," "]], columns=['A','m','k','m'])

print(df1)
