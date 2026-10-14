class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rtrn = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                result = nums[i] + nums[left] + nums[right]
                if result == 0:
                    rtrn.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                    continue
                if result >= 1:
                    right -= 1
                else:
                    left += 1
        return rtrn