class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        outputs = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                i2 = stack.pop()
                outputs[i2] = i - i2
            stack.append(i)

        return outputs
