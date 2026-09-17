class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        diccionario = set()
        
        for n in nums:
            if n in diccionario:
               return True
            diccionario.add(n)       
        return False
        
        
        

        