from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os
import SimpleITK as sitk 
from SimpleITK import GetImageFromArray
import hashlib
from random import *

def handle(request, idImage = ''):
    method = request.method
    if(method == 'DELETE') : 
        delete_image(idImage)
        return HttpResponse(status=200)
    if(method=='GET'):
        return create_image()

def delete_image(idImage):
    os.remove(str(settings.BASE_DIR) +"/app/Storage/image_"+str(idImage)+".nii")

def create_image():
    data_path=str(settings.BASE_DIR)+'/app/Storage' 
    image=sitk.ReadImage("C:/Users/Nicolas/Desktop/Img_Stage/image_1c.nii")
    a=randint(0, 10000)   
    # md5_img=hashlib.md5(a)
    md5_img=str(a)
    # img=sitk.ReadImage("C:/Users/Nicolas/Desktop/Img_Stage/image_1c.nii")        
    # sitk.WriteImage(image,data_path+"/image_"+md5_img+".nii")       
    return HttpResponse(md5_img)

