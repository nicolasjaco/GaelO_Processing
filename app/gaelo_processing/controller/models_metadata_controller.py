import requests
import json

from django.http import HttpResponse, JsonResponse
from django.conf import settings

# from ..models.Idex_model import model_list

def handle(request,model_name):
    method = request.method 
    if(method=='GET'):
        metadata=get_metadata(model_name)
        return JsonResponse(metadata,safe=False)

def get_metadata(model_name):
    metadata=requests.get('http://'+settings.TENSORFLOW_SERVING_ADDRESS+':'+settings.TENSORFLOW_SERVING_METADATA+'/v1/models/'+model_name+'/metadata')
    metadata=metadata.content
    metadata=metadata.decode('utf-8')
    metadata=json.loads(metadata)
    return metadata