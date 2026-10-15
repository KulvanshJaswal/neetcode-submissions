class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
            
        pivot = low
        left = 0
        right = len(nums) - 1

        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1