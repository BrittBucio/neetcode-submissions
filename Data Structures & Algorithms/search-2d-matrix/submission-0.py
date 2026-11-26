class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            rows = len(matrix) # cómo determinamos el len de filas y columnas
            cols = len(matrix[0]) # duda en esto

            l = 0
            r = rows * cols - 1

            while l <= r:

                mid = (l + r) // 2

                row = mid // cols  # por qué aquí es división
                col = mid % cols # por qué aquí es módulo

                # Obtener el valor de la matriz
                value = matrix[row][col]

                if value == target:
                    return True
                elif value < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return False