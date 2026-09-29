class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(index, path, prev_included):
            if index == len(nums):
                ans.append(list(path))
                return

            skip_include = (index > 0 and nums[index] == nums[index - 1]
                and not prev_included)

            if not skip_include:
                path.append(nums[index])
                backtrack(index + 1, path, True)
                path.pop()

            backtrack(index + 1, path, False)

        backtrack(0, [], False)
        return ans