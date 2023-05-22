import numpy as np

import scipy.io

import matplotlib.pyplot as plt




def import_audio_file(path, speaker, word):

    with open(path + '/' + speaker + '/' + word, 'rb') as fid:

    y = np.fromfile(fid, np.int16)

    y = y / max(y)
    return y




def media_arimetica(y):

    u = 0

    N = len(y)

    for n in range(N):

        u += y[n]




    u = u / N

    return u




def desviacion_tipica(y):

    r = 0

    u = media_arimetica(y)

    N = len(y)

    for n in range(N):

        r += (y[n] - u) ** 2




    r = (r / (N - 1)) ** (1/2)

    return r





root_folder = 'C:/Users/Jose Manuel Arias/Documents/stuff/Archivo/hVd_DBase'

file_name = 'hAd.0'




x = import_audio_file(root_folder, 'bill', file_name)




ub = media_arimetica(x)

rb = desviacion_tipica(x)




x = import_audio_file(root_folder, 'david', file_name)




ud = media_arimetica(x)

rd = desviacion_tipica(x)




x = import_audio_file(root_folder, 'kate', file_name)




uk = media_arimetica(x)

rk = desviacion_tipica(x)




x = import_audio_file(root_folder, 'rose', file_name)




ur = media_arimetica(x)

rr = desviacion_tipica(x)




um = [ub, ud]

rm = [rb, rd]




uw = [uk, ur]

rw = [rk, rr]




plt.scatter(um,rm,label='hombres')

plt.scatter(uw,rw,label='mujeres')




plt.xlabel('media')

plt.ylabel('desviación')

plt.title('had: desviación vs media')

plt.grid(True)

plt.legend()

plt.show()