class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        diccionario1 = {}
        diccionario2 = {}

        if len(s) != len(t):
            return False
        
        for c in s:
            diccionario1[c] = diccionario1.get(c, 0) + 1
        
        for c2 in t: 
            diccionario2[c2] = diccionario2.get(c2, 0) + 1


        return diccionario1 == diccionario2
