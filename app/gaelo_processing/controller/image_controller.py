from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os

def handle(request, idImage = ''):
    method = request.method
    if(method == 'DELETE') : 
        delete_image(idImage)
        return HttpResponse(status=200)

def delete_image(idImage):
    os.remove(str(settings.BASE_DIR) +"/app/Storage/image_"+str(idImage)+".nii")
    

