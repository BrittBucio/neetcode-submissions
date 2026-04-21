class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        aux = []
        for i in range(0,len(nums)):  
            # return nums[i] in aux
            if (nums[i] in aux):
                return True
            aux.append(nums[i])
        return False
        
        
        

        