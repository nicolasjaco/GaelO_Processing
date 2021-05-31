from tensorflow_serving.apis import prediction_service_pb2_grpc

from app.gaelo_processing.models.AbstractInference import AbstractInference

class tf_post_process(AbstractInference):

    def post_process(channel,grpc_request):
        stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
        result = stub.Predict(grpc_request,10)        
        resultDict = {}
        for output in result.outputs:
            outputResult = result.outputs[output]
            resultDict[str(output)] = list(outputResult.float_val)
        return resultDict
        