class Solution:
    def search(self, nums: List[int], target: int) -> int:
        inicio, fin = 0, len(nums) - 1
    
        while inicio <= fin:
            medio = (inicio + fin ) // 2
            if nums[medio] > target:
                fin = medio - 1
                medio = (inicio + fin ) // 2
            elif nums[medio] < target:
                inicio = medio + 1
            else:
                return medio
        
        return -1

                