class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")": "(", "]" : "[", "}": "{"}
        
        for caracter in s:
            if caracter in closeToOpen:
                if stack and stack[-1] == closeToOpen[caracter]:
                    stack.pop()
                    print(stack)
                else:
                    return False
            else:
                stack.append(caracter)
                print(stack)
        return True if not stack else False
            
