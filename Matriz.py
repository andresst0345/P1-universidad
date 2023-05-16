import math
import random

class Matriz():

    def __init__(self) -> None:
        pass
    
    def ranvec(self, l= 1) -> list:
        import random as m
        v = [random.randint(-100,100) for vi in range(l)]
        return v
    
    def request_vec(self) -> int:
        