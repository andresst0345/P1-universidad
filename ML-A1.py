import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sc


path= "G:/Torrent/hVd Database/alex"
file_name= "hAd.0"

files = {"hAd.0","haid.0", "haud.0", "hEd.0" }

def import_audio(path: str, file_name: str) -> np.array:

    with open(path + '/' + file_name, 'rb') as fid:
    
        data_array = np.fromfile(fid, np.int16)

        data_array = data_array / max(data_array)

    return data_array


Alex_1 =import_audio(path,file_name)
print(len(Alex_1))
print(Alex_1)






