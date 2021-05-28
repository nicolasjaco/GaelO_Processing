import numpy as np

from PIL import Image

def abstract():
    return


def pre_process():
    img = Image.open('D:/data_docker/inputdata/2.16.840.1.113669.632.20.870421.10000713812_mip_ct.png').convert('LA')
    array = np.array(img).astype('float32')
    array[np.where(array < 185)] = 0 #garder le squelette
    array = array[:,:,0]/255 #normalise
    results=np.reshape(array, (array.shape[0], array.shape[1], 1))
    return results
    