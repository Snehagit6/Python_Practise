class Solution:
    def longestPalindrome(self, s: str) -> str | None:
        if not s:
            return ""
    
        start = 0
        max_length = 1
        
        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
        
            # Return the boundaries of the palindrome found.
            return left + 1, right - 1
        
        for i in range(len(s)):
            # Odd-length palindrome: one center character.
            left1, right1 = expand(i, i)
        
            # Even-length palindrome: two center characters.
            left2, right2 = expand(i, i + 1)
        
            # Update the longest palindrome.
            if right1 - left1 + 1 > max_length:
                start = left1
                max_length = right1 - left1 + 1
        
            if right2 - left2 + 1 > max_length:
                start = left2
                max_length = right2 - left2 + 1
        
        return s[start:start + max_length]
