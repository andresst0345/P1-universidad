import scipy 
import matplotlib as mp
import numpy as np
#
path = "C:/Poyecto PG1/hVd Database-F/bill"
files = ["hAd.0","haid.0", "haud.0", "hEd.0"]
file_name= "hAd.0"
#

def import_audio(path: str, file_name: str) -> np.array:

    with open(path + '/' + file_name, 'rb') as fid:
    
        data_array = np.fromfile(fid, np.int16)

        data_array = data_array / max(data_array)

    return data_array

def energia(v: list) -> float:
    ope = []

    for i in range(len(v)):
        c = v[i] **2
        ope.append(c)

    se = sum(ope)
    eng = se / len(v)

    return eng

def zero_cross(vec) -> float:
    opz = []

    for ii in range(len(vec)):
        b = np.sign(vec[ii]) 
        a = np.sign(vec[ii]-1)
        d = b - a
        opz.append(d)
    
    szc = sum(opz)
    zcr = szc / 2*len(vec)

    return zcr

def entropia(vc: list) -> float:
    opent = []

    for iii in range(len(vc)):
        y = ((vc[iii]) / energia(vc))**2
        z = np.log(y)
        w = y * z
        opent.append(w)

        sent = sum(opent)
        H = sent / len(vc)
    
        return H

#test
k = import_audio(path, file_name)
print("energia ->",energia(k),"\n")
print("zero cross ->",zero_cross(k),"\n")
print("Entropia ->", entropia(k),"\n")


