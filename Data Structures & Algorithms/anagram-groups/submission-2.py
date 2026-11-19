class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diccionario = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in diccionario:
                diccionario[key] = []
            diccionario[key].append(word)
        return list(diccionario.values())