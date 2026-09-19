class Solution:
    def isPalindrome(self, s: str) -> bool:
        limpio = "".join(c.lower() for c in s if c.isalnum())
        j = len(limpio) - 1
        
        for i, letter in enumerate(limpio):
            if limpio[i] != limpio[j]:
                return False
            j -= 1
            if j <= i:
                break

        return True

        # unir la cadena con join 
        # y luego verificar con dos apuntadores o índices de inicio fin, comparar hasta llegar a la mitad, es decir que i=j