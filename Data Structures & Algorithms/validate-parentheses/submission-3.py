class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        setPairs = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for val in s:
            if val in setPairs:
                if stack and stack[-1] == setPairs[val]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        return not stack
