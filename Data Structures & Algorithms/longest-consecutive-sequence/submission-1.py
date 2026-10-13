class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = {}

        longest = 0

        for num in nums:
            numbers[num] = 0

        for num in numbers:
            if num - 1 in numbers:
                continue
            
            temp = 1
            while num + 1 in numbers:
                temp += 1
                num += 1
            longest = max(longest, temp)

        return longest