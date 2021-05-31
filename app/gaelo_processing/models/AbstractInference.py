from abc import ABC, abstractmethod
import grpc
import tensorflow as tf
import numpy as np

from PIL import Image
from google.protobuf.wrappers_pb2 import Int64Value
from tensorflow_serving.apis.model_pb2 import ModelSpec
from tensorflow_serving.apis.predict_pb2 import PredictRequest
from tensorflow_serving.apis import prediction_service_pb2_grpc

from .Inferences.tf_pre_process import tf_pre_process
from .Inferences.tf_post_process import tf_post_process

class AbstractInference():

    def __init__(self,idImage):
        self.idImage=idImage

    # def get_result():
    #     return

    def predict(version:int, model_name:str):
        # appel de pre_process
        pre_pro=tf_pre_process.pre_process()
        channel = grpc.insecure_channel('localhost:8500')        
        version = Int64Value(value=version)
        model_spec = ModelSpec(version=version, name=model_name, signature_name='serving_default')
        grpc_request = PredictRequest(model_spec= model_spec)
        grpc_request.inputs['input_1'].CopyFrom(tf.make_tensor_proto(pre_pro, shape=[1, 503, 136, 1]))
        post_pro=tf_post_process.post_process(channel,grpc_request)
        return post_pro
        #appel de post_process

    @abstractmethod
    def pre_process(self,idImage):
        pass
        #id = 2.16.840.1.113669.632.20.870421.10000713812_mip_ct
        # img = Image.open('D:/data_docker/inputdata/'+idImage+'.png').convert('LA')
        # array = np.array(img).astype('float32')
        # array[np.where(array < 185)] = 0 #garder le squelette
        # array = array[:,:,0]/255 #normalise
        # results=np.reshape(array, (array.shape[0], array.shape[1], 1))
        # return results

    @abstractmethod
    def post_process(self,idImage):
        pass
        # stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
        # result = stub.Predict(grpc_request,10)        
        # resultDict = {}
        # for output in result.outputs:
        #     outputResult = result.outputs[output]
        #     resultDict[str(output)] = list(outputResult.float_val)
        # return resultDict