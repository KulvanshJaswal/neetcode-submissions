class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        outputs = []
        for i in range(len(temps)):
            j = i + 1
            while j < len(temps) and temps[j] <= temps[i]:
                j+=1
            if j >= len(temps):
                outputs.append(0)
            elif temps[j] < temps[i]:
                outputs.append(0)
            else:
                outputs.append(j-i)

        return outputs