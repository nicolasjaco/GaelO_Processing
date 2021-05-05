from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os
import SimpleITK as sitk 
from SimpleITK import GetImageFromArray
import hashlib
from random import *
import base64

def handle(request, idImage = ''):
    method = request.method
    if(method == 'DELETE') : 
        delete_image(idImage)
        return HttpResponse(status=200)
    if(method=='POST'):        
        return create_image(request)

def delete_image(idImage):
    os.remove(str(settings.BASE_DIR) +"/app/Storage/image_"+str(idImage)+".nii")

def create_image(request): 
    data_path=str(settings.BASE_DIR)+'/app/Storage'   
    data = request.read()    
    image_md5 = hashlib.md5(str(data).encode())
    image=base64.b64decode(data)     
    decode_image = open(data_path+'/image_'+image_md5.hexdigest()+'.nii', 'wb')
    decode_image.write(image)
    decode_image.close()          
    return JsonResponse({'image_id':image_md5.hexdigest()})
    
