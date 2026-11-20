# Problem Statement
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal, Panama!"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "Was it a car or a cat I saw?"
# Output: true


def isPalindrome(s: str) -> bool:
    mod_s = ''.join(c.lower() for c in s if c.isalnum())
    return mod_s == mod_s[::-1]
print(isPalindrome("A man, a plan, a canal, Panama!"))  # Output: True
print(isPalindrome("Was it a car or a cat I saw?"))  # Output: True
print(isPalindrome("Hello, World!"))  # Output: False
print(isPalindrome("No 'x' in Nixon"))  # Output: True