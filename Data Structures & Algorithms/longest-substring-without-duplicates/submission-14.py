class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        left = 0
        longest = 1

        for right in range(len(s)):
            chars = s[left:right]
            if chars == "":
                continue
            if s[right] in chars:
                left = left + chars.index(s[right]) + 1
            elif s[right] not in chars:
                longest = max(longest, len(chars) + 1)
                continue

        return longest
