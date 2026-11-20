class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res   # ← antes: return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):              # ← antes: len(str)
            j = i
            while s[j] != "#":         # ← antes: str[j]
                j += 1
            length = int(s[i:j])       # ← antes: str[i:j]
            res.append(s[j + 1: j + 1 + length]) 
            i = j + 1 + length
        return res