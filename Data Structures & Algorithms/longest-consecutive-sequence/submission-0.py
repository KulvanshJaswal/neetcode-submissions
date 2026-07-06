class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        temp = 1 
        numbers = {}
        for num in nums:
            numbers[num] = 1 
        
        for num in numbers:
            if num - 1 in numbers:
                continue
            temp = 1
            while num + 1 in numbers:
                temp += 1
                num += 1
            if temp > longest:
                longest = temp
        return longest