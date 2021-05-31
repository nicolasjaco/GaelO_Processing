import numpy as np
import tensorflow as tf
from django.conf import settings

from PIL import Image
from tensorflow.core.framework.tensor_pb2 import TensorProto
from ..AbstractInference import AbstractInference


class InferenceAcquisitionField(AbstractInference):    

    def pre_process(self, idImage) -> TensorProto:
        #id = 2.16.840.1.113669.632.20.870421.10000713812_mip_ct
        img = Image.open(settings.STORAGE_DIR+'/image/'+idImage+'.png').convert('LA')
        array = np.array(img).astype('float32')
        array[np.where(array < 185)] = 0 #garder le squelette
        array = array[:,:,0]/255 #normalise
        array=np.reshape(array, (array.shape[0], array.shape[1], 1))
        return tf.make_tensor_proto(array, shape=[1, 503, 136, 1])

    def post_process(self, result) -> dict:
        resultDict = {}
        for output in result.outputs:
            outputResult = result.outputs[output]
            resultDict[str(output)] = list(outputResult.float_val)
        return resultDict

    def get_input_name(self) -> str:
        return 'input_1'
    
    def get_model_name(self) -> str:
        return 'aquisition_field_model'
        
