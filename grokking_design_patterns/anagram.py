# Valid Anagram (easy)
# Problem Statement
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

# Example 1:

# Input: s = "listen", t = "silent"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Example 3:

# Input: s = "hello", t = "world"
# Output: false



def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    else:
        return len([s for s in t if s not in t]) == 0

print(isAnagram("listen", "silent"))  # Output: True    
print(isAnagram("rat", "car"))  # Output: False
print(isAnagram("hello", "world"))  # Output: False
print(isAnagram("anagram", "nagaram"))  # Output: True
