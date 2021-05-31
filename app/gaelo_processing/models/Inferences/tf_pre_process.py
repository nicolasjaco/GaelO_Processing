import numpy as np

from PIL import Image
from ..AbstractInference import AbstractInference

class tf_pre_process(AbstractInference):    

    def pre_process(self):
        #id = 2.16.840.1.113669.632.20.870421.10000713812_mip_ct
        img = Image.open('D:/data_docker/inputdata/'+self.value+'.png').convert('LA')
        array = np.array(img).astype('float32')
        array[np.where(array < 185)] = 0 #garder le squelette
        array = array[:,:,0]/255 #normalise
        results=np.reshape(array, (array.shape[0], array.shape[1], 1))
        return results
        
