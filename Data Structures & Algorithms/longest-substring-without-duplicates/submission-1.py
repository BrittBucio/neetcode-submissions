class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0

        window = set()
        maxLenght = 0
        
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            lenght=len(window)
            
            if maxLenght < lenght:
                maxLenght = lenght
        
        return maxLenght
