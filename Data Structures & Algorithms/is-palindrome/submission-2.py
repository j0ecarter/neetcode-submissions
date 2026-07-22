class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        if cleaned[::-1] == cleaned:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("Was it a car or a cat i saw?"))