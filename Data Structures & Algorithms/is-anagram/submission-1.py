class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for value in t:
            if value not in count:
                return False
            count[value] -= 1
            if count[value] == 0:
                del count[value]

        return len(count) == 0
        
        