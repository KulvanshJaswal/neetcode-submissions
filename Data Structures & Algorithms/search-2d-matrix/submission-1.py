class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        while row <= len(matrix) - 1:
            top = len(matrix[row]) - 1
            if target > matrix[row][top]:
                row+=1
            elif target <= matrix[row][top]:
                break

        if row >= len(matrix):
            return False
            
        bottom = 0
        while bottom <= top:
            mid = (bottom + top) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                bottom = mid + 1
            else:
                top = mid - 1
        return False
