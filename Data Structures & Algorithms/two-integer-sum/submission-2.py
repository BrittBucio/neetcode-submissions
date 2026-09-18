class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicc = {}
        for i in range(0,len(nums)):
            inverso = target - nums[i]
            if inverso in dicc:
                print(i,",",inverso)
                return [dicc[inverso],i]
            dicc[nums[i]]=i
        return 