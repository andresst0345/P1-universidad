import numpy as np
import matplotlib
import scipy 

files = ["hid.0", "hId.0", "hEd.0", "hAd.0", "had.0", "hYd.0", "hOd.0", "hod.0", "hUd.0", "hud.0", "hed.0", "heid.0", "haid.0", "haud.0", "hoid.0", "houd.0", "hied.0", "heed.0"]

folders = ["andrew", "andy", "bill", "david", "geoff", "jo", "kate", "mike", "nick", "penny", "rich", "rose", "sarah", "sue", "tim", "wendy"]

path = "C:/Poyecto PG1/hVd Database-F/"

def import_audio(path, file_name):
    with open(path + '/' + file_name, 'rb') as fid:
        data_array = np.fromfile(fid, np.int16)
        data_array = data_array / max(data_array)
    return data_array

def energia(v):
    ope = []
    for i in range(len(v)):
        c = v[i] ** 2
        ope.append(c)
    se = sum(ope)
    eng = se / len(v)
    return eng

def zero_cross(vec):
    opz = []
    for ii in range(len(vec)):
        b = np.sign(vec[ii]) 
        a = np.sign(vec[ii] - 1)
        d = b - a
        opz.append(d)
    szc = sum(opz)
    zcr = szc / (2 * len(vec))
    return zcr

def entropia(vc):
    opent = []
    vc = np.array(vc)  # Convertir la lista a un arreglo de NumPy para facilitar las operaciones vectorizadas
    eng = energia(vc)  
    y = (vc / eng) ** 2

    # Aplicar las operaciones vectorizadas solo a los valores positivos de y
    mask = (y > 0)  # Máscara booleana para valores positivos de y
    y_pos = y[mask]  # Valores positivos de y
    z = np.zeros_like(y)  # Arreglo de ceros del mismo tamaño que y
    z[mask] = np.log(y_pos)  # Calcular el logaritmo solo para los valores positivos de y
    w = y * z

    sent = np.sum(w)  
    H = sent / len(vc)
    return H



def calcular_resultados(files, folders, path):
    resultados = []
    for folder in folders:
        folder_rt = []
        for file in files:
            
            archivo = folder + '/' + file
            vec = import_audio(path, archivo)

            
            rt_zero_cross = zero_cross(vec)
            rt_entropia = entropia(vec)
            rt_energia = energia(vec)

            folder_rt.append((rt_energia, rt_zero_cross, rt_entropia))

        resultados.append(folder_rt)

    return resultados

# 
resultados = calcular_resultados(files, folders, path)

rt_C0_A0 = resultados[0][0]
energia_C0_A0 = rt_C0_A0[0]
zero_cross_C0_A0 = rt_C0_A0[1]
entropia_C0_A0 = rt_C0_A0[2]

# carpeta  1 - archivo 2

rt_C1_A2 = resultados [1][2]
energia_C1_A2 = rt_C1_A2 [0]
zero_cross_C1_A2 = rt_C1_A2 [1]
entropia_C1_A2 = rt_C1_A2 [2]

# 

print("Resultados Carpeta 0 Archivo 0 = " ,"\n")
print("Energía ->", energia_C0_A0 ,"\n")
print("Zero Cross ->", zero_cross_C0_A0 ,"\n")
print("Entropía ->", entropia_C0_A0 ,"\n")

print(f"Resultados Carpeta 1 Archivo 2 =","\n" )
print(f"Energía ->", energia_C1_A2 ,"\n")
print(f"Zero Cross ->", zero_cross_C1_A2 ,"\n")
print(f"Entropía ->", entropia_C1_A2 ,"\n")
