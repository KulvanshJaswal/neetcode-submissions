class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(index, path):
            if index == len(nums):
                if list(path) not in ans:
                    ans.append(list(path))
                return

            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()
            backtrack(index+1,path)
        backtrack(0,[])

        return ans
