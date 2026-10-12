class Solution:
    def isValid(self, s: str) -> bool:
        dicc = {")": "(", "]": "[", "}": "{"}   # cierre → apertura
        pila = []

        for c in s:
            if c in dicc:                        # es un cierre
                if not pila or pila[-1] != dicc[c]:
                    return False
                pila.pop()
            else:                                # es una apertura
                pila.append(c)

        return not pila                          # sin aperturas huérfanas