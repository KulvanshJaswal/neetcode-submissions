class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        left = 0
        right = 1
        longest = 1

        while right < len(s):
            if left == right:
                right += 1
            elif s[right] in s[left:right]:
                left += 1
            else:
                longest = max(longest, right - left + 1)
                right += 1

        return longest
