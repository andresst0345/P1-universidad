import scipy 
import matplotlib as mp
import numpy as np

files = {"hAd.0","haid.0", "haud.0", "hEd.0" }



path= "G:/Torrent/hVd Database/alex"
file_name= "hAd.0"

def import_audio(path: str, file_name: str) -> np.array:

    with open(path + '/' + file_name, 'rb') as fid:
    
        data_array = np.fromfile(fid, np.int16)

        data_array = data_array / max(data_array)

    return data_array


