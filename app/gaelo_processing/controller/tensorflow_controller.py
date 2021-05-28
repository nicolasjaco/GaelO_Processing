from django.http import JsonResponse

from ..models.AbstractInference import AbstractInference

def handle(request, model_name=''):
    method = request.method
    if(method == 'POST'):
        idImage=request.read()
        tensorflow_response=model(idImage,model_name)
        return JsonResponse(tensorflow_response)

def model(idImage, model_name):
     #instancier correctement en appeleant la bonne méthode
    return AbstractInference.get_result(idImage,model_name)