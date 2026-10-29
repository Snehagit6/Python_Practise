# Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

import sys
import os
import inspect
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BigOnotation.perf_ai import get_perf_ai_response

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for each in range(len(haystack)):
            if needle in haystack[each:each+len(needle)]:
                return each
        return -1
        

response = get_perf_ai_response(program=inspect.getsource(Solution().strStr))
print(type(response))
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "longest_st_no_dup.txt")
with open(output_file_path, "w", encoding='utf-8') as f:
    f.write(response)