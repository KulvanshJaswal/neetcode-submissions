class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        
        def backtrack(start_index, current_target, temp):
            if current_target == 0:
                ans.append(list(temp))
                return
            
            if current_target < 0:
                return
            
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                num = candidates[i]
                if num > current_target:
                    break
                    
                temp.append(num)
                backtrack(i + 1, current_target - num, temp)
                temp.pop()

        backtrack(0, target, [])
        return ans       