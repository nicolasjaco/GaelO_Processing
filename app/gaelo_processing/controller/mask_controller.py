from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os

from django.conf import settings


def handle(request, idMask = ''):
    print(settings.SITE_ROOT)
    method = request.method
    if(method == 'DELETE') : 
        delete_mask(resquest, idMask)
        return HttpResponse(status=200)   
    if(method=='POST'):
        create_mask()     


def delete_mask(resquest, idMask):
    os.remove(str(settings.BASE_DIR)+"/app/Storage//mask_"+str(idMask)+".nii")

def create_mask():
    return HttpResponse("hello")