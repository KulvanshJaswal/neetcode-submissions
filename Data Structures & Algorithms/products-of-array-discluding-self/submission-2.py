class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        prefix = 1
        for i in range(len(nums)):
            left.append(prefix)
            prefix *= nums[i]
        prefix = 1
        for j in range(len(nums)-1, -1, -1):
            right.append(prefix)
            prefix *= nums[j]

        return [left[i]*right[len(nums)-i-1] for i in range(len(nums))]

