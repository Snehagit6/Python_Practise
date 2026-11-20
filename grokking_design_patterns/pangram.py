
# Problem Statement
# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing English letters (lower or upper-case), return true if sentence is a pangram, or false otherwise.

# Note: The given sentence might contain other characters like digits or spaces, your solution should handle these too.

# Example 1:

# Input: sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"
# Output: true
# Explanation: The sentence contains at least one occurrence of every letter of the English alphabet either in lower or upper case.
# Example 2:

# Input: sentence = "This is not a pangram"
# Output: false
# Explanation: The sentence doesn't contain at least one occurrence of every letter of the English alphabet.
# Example 3:

# Input: sentence = "abcdefghijklmnopqrstuvwxy1"
# Output: false
# Explanation: The digit is not a letter, so it does not count towards the alphabet. Only a through y are
# present and z is missing, so this is not a pangram.



import string
def isPangram(sentence: str) -> bool:
    unique_letters = set()
    for char in sentence:
        if char.isalpha():
            unique_letters.add(char.lower())
    return len(unique_letters) == len(string.ascii_lowercase)

'''
dir(string): >>> dir(string)
['Formatter', 'Template', '_TemplatePattern', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_sentinel_dict', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz
'''

print(isPangram("TheQuickBrownFoxJumpsOverTheLazyDog"))  # Output: True
print(isPangram("This is not a pangram"))  # Output: False
print(isPangram("abcdefghijklmnopqrstuvwxy1"))  # Output: False
