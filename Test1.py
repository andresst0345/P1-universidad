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
    for iii in range(len(vc)):
        y = ((vc[iii]) / energia(vc)) ** 2
        if y <= 0:  
            w = np.nan  # Asignar un valor predeterminado, por ejemplo, np.nan
        else:
            z = np.log(y)
            w = y * z
        opent.append(w)
    sent = sum(opent)
    H = sent / len(vc)
    return H


def calcular_resultados(files, folders, path):
    resultados = []
    for folder in folders:
        folder_resultados = []
        for file in files:
            
            archivo = folder + '/' + file
            vector = import_audio(path, archivo)

            
            resultado_zero_cross = zero_cross(vector)
            resultado_entropia = entropia(vector)
            resultado_energia = energia(vector)

            folder_resultados.append((resultado_energia, resultado_zero_cross, resultado_entropia))

        resultados.append(folder_resultados)

    return resultados

# 
resultados = calcular_resultados(files, folders, path)

resultados_carpeta0_archivo0 = resultados[0][0]
energia_carpeta0_archivo0 = resultados_carpeta0_archivo0[0]
zero_cross_carpeta0_archivo0 = resultados_carpeta0_archivo0[1]
entropia_carpeta0_archivo0 = resultados_carpeta0_archivo0[2]

# Acceder a los resultados de la carpeta en la posición 1 y el archivo en la posición 2
resultados_carpeta1_archivo2 = resultados[1][2]
energia_carpeta1_archivo2 = resultados_carpeta1_archivo2[0]
zero_cross_carpeta1_archivo2 = resultados_carpeta1_archivo2[1]
entropia_carpeta1_archivo2 = resultados_carpeta1_archivo2[2]

# Imprimir los resultados
print("Resultados Carpeta 0 Archivo 0:")
print("Energía:", energia_carpeta0_archivo0)
print("Zero Cross:", zero_cross_carpeta0_archivo0)
print("Entropía:", entropia_carpeta0_archivo0)

print("Resultados Carpeta 1 Archivo 2:")
print("Energía:", energia_carpeta1_archivo2)
print("Zero Cross:", zero_cross_carpeta1_archivo2)
print("Entropía:", entropia_carpeta1_archivo2)
