class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        for i in range(0, len(heights) - 1):
            for j in range(i+1, len(heights)):
                height = min(heights[i], heights[j])
                temp = height * (j - i)
                if temp > volume:
                    volume = temp
        return volume