#Sorting helps in binary search
import sys
import os
import inspect

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BigOnotation.perf_ai import get_perf_ai_response

l = [12,7,39,34,53,72]
def selection_sort(l):
    """
    In selection sort, we repeatedly find the minimum element from the unsorted part of the list and move it to the beginning. The algorithm maintains two subarrays in a given array:
1. The subarray which is already sorted.
    """

    for i in range(len(l) - 1):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l

print(selection_sort(l))
response = get_perf_ai_response(program=inspect.getsource(selection_sort))
print(type(response))
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Selection_sort.txt")
with open(output_file_path, "w", encoding='utf-8') as f:
    f.write(response)