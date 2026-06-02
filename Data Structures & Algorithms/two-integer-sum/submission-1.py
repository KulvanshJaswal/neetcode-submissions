class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i, num in enumerate(nums):
            targeted = target - num
            if targeted in numbers:
                return [numbers[targeted], i]
            numbers[num] = i
            
            
        