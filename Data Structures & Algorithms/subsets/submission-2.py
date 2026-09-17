class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(index, path):
            if index == len(nums):
                ans.append(list(path))
                return

            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()
            backtrack(index+1,path)
        backtrack(0,[])

        return ans