class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            result = (numbers[left] + numbers[right]) - target

            if result == 0:
                return [left + 1, right + 1]

            if result >= 1:
                right -= 1
            else:
                left += 1