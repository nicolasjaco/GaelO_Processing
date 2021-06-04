import numpy as np
import tensorflow as tf
from django.conf import settings

from PIL import Image
from tensorflow.core.framework.tensor_pb2 import TensorProto
from ..AbstractInference import AbstractInference


class InferenceAcquisitionField(AbstractInference):  

    def pre_process(self, idImage:str) -> TensorProto:
        """[summary]

        Args:
            idImage (str): [description]

        Returns:
            TensorProto: [description]
        """
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
            
        dict={}
        #lef_arm down true/false
        if resultDict['left_arm'][0]>resultDict['left_arm'][1]:
            left_arm=True
        else :
            left_arm=False
        #right_arm down true/false
        if resultDict['right_arm'][0]>resultDict['right_arm'][1]:
            right_arm=True
        else :
            right_arm=False
        #vertex true/false
        if resultDict['head'][0]>resultDict['head'][1]:
            head=True
        else :
            head=False

        for i in range(len(resultDict['leg'])):
            if resultDict['leg'][i] >0.5 :
                if(i == 0) : leg='Hips'
                if(i == 1) : leg='Knee'
                if(i == 2) : leg='Foot'

        dict={'left_arm_down':left_arm,'right_arm_down':right_arm,'head':head,'leg':leg}
        
        return dict

    def get_input_name(self) -> str:
        return 'input_1'
    
    def get_model_name(self) -> str:
        return 'aquisition_field_model'
        
