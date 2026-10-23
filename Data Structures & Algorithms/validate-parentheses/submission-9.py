class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {")": "(", "]": "[", "}": "{"}

        for val in s:
            if val in close:
                if stack and stack[-1] == close[val]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        
        if not stack:
            return True
        else:
            return False
            