import math
import random

class Matriz():

    def __init__(self,f ,c ,v1 ,v2 ) -> None:
        self.f = filas
        self.c = columnas
        self.v1 = vector1 

        
    
    def ranvec(self, f= 1, c= 1) -> list:
        import random as m
        mtz = []
        for i in range(c):
         fil = [random.randint(-100,100) for vi in range(f)]
         mtz.append(fil)
        return mtz
    
    def sumvec(self ,v1 ,v2 ) -> list:
        suma = []
        for i in range(len(v1)):
            suma.append(v1[i] + v2[i])
        return suma
    

#test func

v = ranvec(4, 4)

