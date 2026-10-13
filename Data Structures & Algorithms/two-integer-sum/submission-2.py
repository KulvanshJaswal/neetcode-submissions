class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}

        for i, num in enumerate(nums):
            wanted = target - num

            if wanted in targets:
                return [targets[wanted], i]
            targets[num] = i