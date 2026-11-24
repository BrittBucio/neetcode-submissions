class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = height * width
        # height = min (height[left], height[right])
        # witdh = right - left


        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            height = min (heights[left], heights[right])
            witdh = right - left
            area = height * witdh 
            maxArea = max(maxArea, area)
        
            if heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1
        
        return maxArea

