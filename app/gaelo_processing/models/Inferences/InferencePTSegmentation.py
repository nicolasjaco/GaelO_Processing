
from tensorflow.core.framework.tensor_pb2 import TensorProto
from ..AbstractInference import AbstractInference

class InferencePTSegmentation(AbstractInference):  

    def pre_process(self, idImage:str) -> TensorProto:
        return

    def post_process(self, result) -> dict:
        return

    def get_input_name(self) -> str:
        return 'input_1'
    
    def get_model_name(self) -> str:
        return 'PT_segmentation'