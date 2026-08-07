class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 if s == "" else 1

        left = 0 
        
        for right in range(len(s)):
            chars = s[left:right]
            if chars == "":
                continue
            if s[right] in chars:
                left = left + chars.index(s[right]) + 1

            elif s[right] not in chars:
                longest = len(chars) + 1 if len(chars) + 1 > longest else longest
                continue
        return longest