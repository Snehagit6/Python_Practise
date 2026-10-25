# Sorting helps in binary search

import sys
import os
import inspect

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BigOnotation.perf_ai import get_perf_ai_response


def lengthOfLongestSubstring(s: str) -> int:
    """
    O(n) time, O(min(m, n)) space where m = size of character set
    (for ASCII m = 128, for Unicode it can be larger).
    """
    last_pos = {}         # char -> last index where it appeared
    left = 0              # start of the current window
    max_len = 0

    for right, ch in enumerate(s):
        # If ch was seen inside the current window, move `left`
        if ch in last_pos and last_pos[ch] >= left:
            left = last_pos[ch] + 1

        # Update the last seen position of ch
        last_pos[ch] = right

        # Window length is right - left + 1
        max_len = max(max_len, right - left + 1)

    return max_len

response = get_perf_ai_response(program=inspect.getsource(lengthOfLongestSubstring))
print(type(response))
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "longest_st_no_dup.txt")
with open(output_file_path, "w", encoding='utf-8') as f:
    f.write(response)
