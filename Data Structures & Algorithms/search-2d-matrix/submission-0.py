class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            row = (l+r) // 2
            if matrix[row][0] == target:
                return True
            elif matrix[row][0] > target:
                r = row - 1
            else:
                l = row + 1
        row = r
        l = 0
        r = len(matrix[r]) - 1
        while l <= r:
            cell = (l+r) // 2
            if matrix[row][cell] > target:
                r = cell - 1
            elif matrix[row][cell] < target:
                l = cell + 1
            else:
                return True
        return False