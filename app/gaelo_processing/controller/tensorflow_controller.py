import json
import importlib

from django.http import JsonResponse
import tensorflow

from ..models.Inferences.InferenceAcquisitionField import InferenceAcquisitionField

def handle(request, model_name=''):
    method = request.method
    if(method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        tensorflow_response=model(body['id'],model_name)
        print(JsonResponse(tensorflow_response))
        return JsonResponse(tensorflow_response)

def model(idImage:str, model_name:str): 
    inferenceInstance = getInferenceModel(model_name)
    results=inferenceInstance.predict(idImage)
    return results

def getInferenceInstanceByName(class_name):
    module = getattr(importlib.import_module("app.gaelo_processing.models.Inferences"), class_name)
    InferenceClass = getattr(module, class_name)
    return InferenceClass()

def getInferenceModel(model_name):
    model_list = {
        'aquisition_field_model' : 'InferenceAcquisitionField'
    }

    return getInferenceInstanceByName(model_list[model_name])