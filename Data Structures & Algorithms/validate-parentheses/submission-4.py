class Solution:
    def isValid(self, s: str) -> bool:      
        stack = []

        convert = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for char in s:
            if not stack:
                stack.append(char)
                continue
            if char in ["[", "{", "("]:
                stack.append(char)
            else:
                if convert[char] != stack[-1]:
                    return False
                if convert[char] == stack[-1]:
                    stack.pop()

        if stack:
            return False
        return True