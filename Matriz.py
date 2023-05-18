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
    
    def sumvec(self ,m1 ,m2 ) -> list:
        if len(m1) != len(m2):
            raise ValueError("Las matrices deben tener el mismo tamaño")
        suma = []
        for ii in range(len(m1)):
           fil = []
           for j in range(len(m1)):
              fil.append(m1[ii][j] + m2[ii][j])
           suma.append(fil)

    

#test func

v = ranvec(4, 4)

