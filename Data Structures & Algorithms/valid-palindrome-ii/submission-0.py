class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        for i in range(len(s)):
            next_val = i+1
            newS = s[:i] + s[next_val:]
            if newS == newS[::-1]:
                return True

        return False 
        