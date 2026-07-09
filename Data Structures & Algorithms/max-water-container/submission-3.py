class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            height = min(heights[i], heights[j])
            temp = height * (j-i)
            if temp > volume:
                volume = temp
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return volume