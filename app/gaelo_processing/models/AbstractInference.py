from abc import abstractmethod
import grpc
import tensorflow as tf

from google.protobuf.wrappers_pb2 import Int64Value
from tensorflow_serving.apis.model_pb2 import ModelSpec
from tensorflow_serving.apis.predict_pb2 import PredictRequest
from tensorflow_serving.apis import prediction_service_pb2_grpc

class AbstractInference :

    def __init__(self,idImage):
        self.idImage=idImage

    def get_result():
        return

    def predict(version, model_name):
        channel = grpc.insecure_channel('localhost:8500')
        stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
        version = Int64Value(value=version)
        model_spec = ModelSpec(version=version, name=model_name, signature_name='serving_default')
        grpc_request = PredictRequest(model_spec= model_spec)
        grpc_request.inputs['input_1'].CopyFrom(tf.make_tensor_proto(array, shape=[1, 503, 136, 1]))

    @abstractmethod
    def abstarct_methode(idImage):
        return