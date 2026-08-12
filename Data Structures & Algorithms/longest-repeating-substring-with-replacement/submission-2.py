class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0  
        left = 0 

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
            
            window = right - left + 1
            flips = window - max(count.values())

            while flips > k:
                count[s[left]] -= 1
                left += 1
                window = right-left+1
                flips = window - max(count.values())
            longest = max(longest, (right-left + 1))
        return longest