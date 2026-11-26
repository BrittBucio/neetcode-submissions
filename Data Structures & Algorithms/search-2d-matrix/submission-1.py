class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bottom = len(matrix) - 1 # num de filas - 1 para indice

        # Primera búsqueda: encontrar la fila
        while top <= bottom:

            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                bottom= mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                row = mid
                break
        else:
            return False

        # Segunda búsqueda: encontrar el elemento
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:

            mid = (left + right) // 2

            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True
        
        return False
