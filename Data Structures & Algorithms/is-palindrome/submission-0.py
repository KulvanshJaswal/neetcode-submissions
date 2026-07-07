class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(filter(str.isalnum, s))
        s = "".join(s.split())
        temp = s[::-1]

        return s == temp
