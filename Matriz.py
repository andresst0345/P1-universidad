import random

class Matriz():
    import math
    

    def __init__(self,f: int ,c: int ,v1:list ,v2: list ) -> None:
        self.f = f
        self.c = c
        self.v1 = v1
        self.v2 = v2

        
    def ranvec(self, f= 1, c= 1) -> list:# vector alatorio n*n
        import random as m
        mtz = []
        for i in range(c):
         fil = [random.randint(-100,100) for vi in range(f)]
         mtz.append(fil)
        return mtz
    
    def summt(self ,m1 ,m2 ) -> list: #suma
        if len(m1) != len(m2):
            raise ValueError("Las matrices deben tener el mismo tamaño")
        suma = []
        for ii in range(len(m1)):
           fil = []
           for j in range(len(m1)):
              fil.append(m1[ii][j] + m2[ii][j])
           suma.append(fil)

    def restmt(self, m1, m2) -> list: #resta
        if len(m1) != len(m2):
            raise ValueError("Las matrices deben tener el mismo tamaño")
        rest = []
        for ii in range(len(m1)):
           fil = []
           for j in range(len(m1)):
              fil.append(m1[ii][j] - m2[ii][j])
           rest.append(fil)
        return rest

    def multvec(self,m1 ,m2 ) -> list: #multiplicacion
        mult = []
        if len(m1[0]) != len(m2):
            raise ValueError("El número de columnas de la matriz1 debe ser igual al número de filas de la matriz2")
        fil_m1 = len(m1)
        col_m1 = len(m1[0])
        col_m2 = len(m2[0])
        

        return mult
    
    def divmt(self, m1, m2):




        return pass
#test func

v = ranvec(4, 4)

