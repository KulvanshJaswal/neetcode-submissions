class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        row = 0
        while row < num_rows:
            if target > matrix[row][num_cols - 1]:
                row += 1
            else:
                break
                
        if row >= num_rows:
            return False
            
        left = 0
        right = num_cols - 1
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False