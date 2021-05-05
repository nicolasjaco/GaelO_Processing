from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..adapter.pyradiomics_adapter import pyradiomics_adapter
from ..data_object import conversion
import SimpleITK as sitk 
from SimpleITK import GetImageFromArray
import os
import numpy as np
from radiomics import featureextractor
import json
from json import JSONEncoder
from ..data_object.pyradiomics_response import NumpyArrayEncoder
from django.conf import settings
from jsonschema import SchemaError

#On teste si c est une methode POST ou GET
def handle(request, idImage = '' , idMask = '', idJson=''):
    method = request.method
    if(method == 'GET') : 
        return get_radiomics(request, idImage, idMask, idJson)
    if(method == 'POST') : 
        return post_radiomics(request, idImage, idMask, idJson)

#Pour pouvoir vérifier l'affichage en web mais a del par la suite
def get_radiomics(request, idImage, idMask, idJson):
    image=str(settings.BASE_DIR)+"/app/Storage/image_"+str(idImage)+".nii"     
    mask=str(settings.BASE_DIR)+"/app/Storage/mask_"+str(idMask)+".nii"   
  
    #On verifie que les images existent: 
    try :
        image=sitk.ReadImage(image)
        mask=sitk.ReadImage(mask)

    except RuntimeError as re:
        status_code=str(400)
        message=str(re)                  
        return HttpResponse("Error_Code: "+status_code +" Error_Message: "+ message)

    if mask.GetDimension()!=image.GetDimension():
        mask=conversion.convert(image,mask)

    try:        
        pyradiomics_adapter_instance = pyradiomics_adapter()
        # pyradiomics_adapter_instance.set_img()
        # pyradiomics_adapter_instance.set_mask()            
        pyradiomics_response = pyradiomics_adapter_instance.calculate(image, mask, idJson)    
        return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder, json_dumps_params={'indent': 4})            

    except ValueError as ve:
        status_code= str(400)
        message= str(ve)            
        return HttpResponse("Error_Code: "+status_code +" Error_Message: "+ message)               

def post_radiomics(request, idImage, idMask, idJson):
    image=str(settings.BASE_DIR)+"/app/Storage/image_"+str(idImage)+".nii"     
    mask=str(settings.BASE_DIR)+"/app/Storage/mask_"+str(idMask)+".nii"
    id_img = int(idImage)
    id_mask=int(idMask)
    id_Json=int(idJson)
    
    #On verifie que les images existent: 
    try :
        image=sitk.ReadImage(image)
        mask=sitk.ReadImage(mask) 

    except RuntimeError as re:
        status_code=str(400)
        message=str(re)
        print(re)            
        return HttpResponse("Error_Code: "+status_code +" Error_Message: "+ message)

    #Si le mask n'est pas de la même dimension que l'image on la convertie
    if mask.GetDimension()!=image.GetDimension():
        mask=conversion.convert(image,mask)

    try:        
        pyradiomics_adapter_instance = pyradiomics_adapter()
        # pyradiomics_adapter_instance.set_img()
        # pyradiomics_adapter_instance.set_mask()
        pyradiomics_response = pyradiomics_adapter_instance.calculate(image,mask,idJson)    
        return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder, json_dumps_params={'indent': 4})

    except ValueError as ve:
        status_code= str(400)
        message= str(ve)            
        return HttpResponse("Error_Code: "+status_code +" Error_Message: "+ message)      