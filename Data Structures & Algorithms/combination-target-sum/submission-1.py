class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
    
        def backtrack(start_index, current_target, temp):
            if current_target == 0:
                ans.append(list(temp))
                return
            
            if current_target < 0:
                return
            
            for i in range(start_index, len(nums)):
                num = nums[i]
                temp.append(num)
                backtrack(i, current_target - num, temp)
                temp.pop()

        backtrack(0, target, [])
        return ans