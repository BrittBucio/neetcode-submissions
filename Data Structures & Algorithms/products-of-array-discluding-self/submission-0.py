class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
         output = [1] * len(nums)
         prefijo, sufijo = 1, 1 # por qué en 1?

         for i in range (len(nums)):
            output[i] = prefijo
            prefijo *= nums[i]
        
         for i in range(len(nums) - 1, -1, -1):
            output[i] *= sufijo
            sufijo *= nums[i]

         return output