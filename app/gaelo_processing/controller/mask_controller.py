from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os
import SimpleITK as sitk 
from SimpleITK import GetImageFromArray
import hashlib
from random import *
import base64

def handle(request, idMask = ''):    
    method = request.method
    if(method == 'DELETE') : 
        delete_mask(idMask)
        return HttpResponse(status=200)   
    if(method=='POST'):
        return create_mask(request)
        
def delete_mask(idMask):
    os.remove(str(settings.BASE_DIR)+"/app/Storage/mask_"+str(idMask)+".nii")

def create_mask(request):
    data_path=str(settings.BASE_DIR)+'/app/Storage'   
    data = request.read()
    mask_md5 = hashlib.md5(str(data).encode())
    mask=base64.b64decode(data)  
    decode_mask = open(data_path+'/mask_'+mask_md5.hexdigest()+'.nii', 'wb')
    decode_mask.write(mask)
    decode_mask.close()          
    return JsonResponse({'mask_id': mask_md5.hexdigest()})