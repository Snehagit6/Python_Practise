import sys
import os
import inspect

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BigOnotation.perf_ai import get_perf_ai_response

def return_ls(input_ls):
    msg = ""
    # Replace with a more efficient sorting algorithm if needed
    # sorted(input_ls, key=lambda x: (x[0] != 'a', x[-1] == 'z'))
    for each in range(len(input_ls)-1):
        if input_ls[each][0]!='a' and input_ls[each+1][0] == 'a':
            input_ls[each], input_ls[each+1] = input_ls[each+1], input_ls[each]

        elif input_ls[each][-1]== 'z' and input_ls[each+1][-1] !='z':
            input_ls[each], input_ls[each+1] = input_ls[each+1], input_ls[each]
    
    for each in input_ls:
        if msg and msg[-1] == each[0]:
            msg = msg + each[1:]
        else:
            msg = msg + each
    return msg
        
    
# input_ls=["klc", "abc", "chz", "cpm"]    
# print(sorted(input_ls, key=lambda x: (x[0] != 'a', x[-1] == 'z')))
# print(return_ls(input_ls=["klc", "abc", "chz", "cpm"]))

print(get_perf_ai_response(program=inspect.getsource(return_ls)))