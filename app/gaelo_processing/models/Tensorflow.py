import grpc
import tensorflow as tf
import numpy as np
import json


from PIL import Image
# from django.forms.fields import JSONString
from google.protobuf.wrappers_pb2 import Int64Value
from tensorflow_serving.apis.model_pb2 import ModelSpec
from tensorflow_serving.apis.predict_pb2 import PredictRequest
from tensorflow_serving.apis import prediction_service_pb2_grpc


class Tensorflow:
    def predict(self, model_name:str , version:int):
        #execute inference
        channel = grpc.insecure_channel('localhost:8500')
        stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
        version = Int64Value(value=version)
        model_spec = ModelSpec(version=version, name=model_name, signature_name='serving_default')
        grpc_request = PredictRequest(model_spec= model_spec)
        #execute inference

        #pre process
        img = Image.open('D:/data_docker/inputdata/2.16.840.1.113669.632.20.870421.10000713812_mip_ct.png').convert('LA')
        array = np.array(img).astype('float32')
        array[np.where(array < 185)] = 0 #garder le squelette
        array = array[:,:,0]/255 #normalise
        np.reshape(array, (array.shape[0], array.shape[1], 1))
        #fin pre process
        
        #execute inference
        grpc_request.inputs['input_1'].CopyFrom(tf.make_tensor_proto(array, shape=[1, 503, 136, 1]))

        #post process
        result = stub.Predict(grpc_request,10)
        # print(result)
        resultDict = {}
        for output in result.outputs:
            outputResult = result.outputs[output]
            resultDict[str(output)] = list(outputResult.float_val)

        # print(json.dumps(resultDict))
        
