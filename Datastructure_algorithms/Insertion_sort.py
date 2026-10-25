# Sorting helps in binary search
import sys
import os
import inspect

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BigOnotation.perf_ai import get_perf_ai_response


l = [2, 73, 89, 4, 0]

def insertion_sort(l):

    for i in range(len(l)):
        min_pos = i

        while min_pos > 0 and l[min_pos] < l[min_pos-1]:

            l[min_pos], l[min_pos-1] = l[min_pos-1], l[min_pos]
            min_pos = min_pos - 1
    return l

print(insertion_sort(l))

response = get_perf_ai_response(program=inspect.getsource(insertion_sort))
print(type(response))
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "longest_st_no_dup.txt")
with open(output_file_path, "w", encoding='utf-8') as f:
    f.write(response)