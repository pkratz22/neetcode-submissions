class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            row = (top+bottom) // 2
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break

        if not (top <= bottom):
            return False
        row = (top + bottom) // 2

        l = 0
        r = len(matrix[row]) - 1

        while l <= r:
            cell = (l+r) // 2
            if matrix[row][cell] > target:
                r = cell - 1
            elif matrix[row][cell] < target:
                l = cell + 1
            else:
                return True
        return False