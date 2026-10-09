from heapq import nlargest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diccionario = {}

        for numero in nums:
            if numero not in diccionario.keys():
                diccionario[numero] = 1
            else: 
                diccionario[numero] += 1

        for n in nums:
            diccionario[n] = diccionario.get(n, 0) + 1
        
        return nlargest(k, diccionario, key=diccionario.get)
        