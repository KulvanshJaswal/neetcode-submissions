class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        outputs = [0] * len(temps)
        stack = []
        for i, temp in enumerate(temps):
            while stack and temp > temps[stack[-1]]:
                i2 = stack.pop()
                outputs[i2] = i - i2
            stack.append(i)
        return outputs