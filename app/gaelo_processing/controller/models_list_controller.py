from django.http import HttpResponse, JsonResponse

from ..models.Idex_model import model_list

def handle(request):
    method = request.method 
    if(method=='GET'):
        list=model_list
        return JsonResponse(list)

