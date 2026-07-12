class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        current_max = 0
        for i in range(n):
            max_left[i] = current_max
            current_max = max(current_max, height[i])

        current_max = 0
        for i in range(n - 1, -1, -1):
            max_right[i] = current_max
            current_max = max(current_max, height[i])


        water = [0] * n
        for i in range(n):
            water[i] = min(max_left[i], max_right[i]) - height[i]
        
        total = 0

        for i in range(n):
            if water[i] > 0:
                total += water[i]

        return total
                