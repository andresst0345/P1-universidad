import math
import random

class Matriz():

    def __init__(self) -> None:
        pass
    
    def ranvec(self, f= 1, c= 1) -> list:
        import random as m
        v = [random.randint(-100,100) for vi in range(f)]
        return v
    
    def sumvec(self ,v1 ,v2 ) -> list:
        suma = []
        for i in range(len(v1)):
            suma.append(v1[i] + v2[i])
        return suma