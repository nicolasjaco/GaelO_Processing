import json
import importlib

from django.http import JsonResponse

from ..models.Inferences import InferenceAcquisitionField #import required

def handle(request, model_name=''):
    method = request.method
    if(method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        tensorflow_response=prediction(body['id'],model_name)
        print(tensorflow_response)
        return JsonResponse(tensorflow_response)

def prediction(idImage:str, model_name:str): 
    inferenceInstance = __getInferenceModel(model_name)
    results=inferenceInstance.predict(idImage)
    return results

def __getInferenceInstanceByName(class_name):
    module = getattr(importlib.import_module("app.gaelo_processing.models.Inferences"), class_name)
    InferenceClass = getattr(module, class_name)
    return InferenceClass()

def __getInferenceModel(model_name):
    model_list = {
        'aquisition_field_model' : 'InferenceAcquisitionField'
    }

    return __getInferenceInstanceByName(model_list[model_name])