from collections import deque

class MyStack:

    def __init__(self):
        # Inicializamos nuestra única cola
        self.queue = deque()

    def push(self, x: int) -> None:
        # 1. Agregamos el nuevo elemento al final de la cola
        self.queue.append(x)
        
        # 2. Rotamos la cola para que el nuevo elemento quede al frente.
        # Movemos todos los elementos que estaban antes detrás del nuevo.
        for _ in range(len(self.queue) - 1):
            # Sacamos del frente y metemos al final
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # Como ya lo reordenamos en el push, el "top" de la pila
        # está realmente al frente de nuestra cola.
        return self.queue.popleft()

    def top(self) -> int:
        # El frente de la cola es el tope de nuestra pila ficticia
        return self.queue[0]

    def empty(self) -> bool:
        # Si la cola no tiene elementos, la pila está vacía
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()