from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..adapter.pyradiomics_adapter import pyradiomics_adapter
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
    id_img = int(idImage)
    id_mask=int(idMask)
    id_Json=int(idJson)

    #On verifie que les images existent: 
    try :
        img_pt=sitk.ReadImage(image)
        img_mask=sitk.ReadImage(mask)

    except RuntimeError as re:
        status_code=str(400)
        message=str(re)
        print(re)            
        return HttpResponse("Error_Code: "+status_code +" Error_Message: "+ message)

# Conversion mask 4D en mask 3D
    if img_mask.GetDimension()==4:
    
        origin = img_pt.GetOrigin()
        direction = img_pt.GetDirection()
        spacing = img_pt.GetSpacing()

        img_mask_array = sitk.GetArrayFromImage(img_mask)
        mask_3D=img_mask_array[1,:,:,:]
        mask_3D=GetImageFromArray(mask_3D)

        mask_3D.SetOrigin(origin)
        mask_3D.SetSpacing(spacing)
        mask_3D.SetDirection(direction)
#Fin Conversion

    # print(request.body)
    if idImage==id_img and idMask==id_mask and id_mask==id_img and idJson==id_Json and id_img==id_Json:
        try:        
            pyradiomics_adapter_instance = pyradiomics_adapter()
            # pyradiomics_adapter_instance.set_img()
            # pyradiomics_adapter_instance.set_mask()            
            pyradiomics_response = pyradiomics_adapter_instance.calculate(img_pt,mask_3D,idJson)    
            return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder, json_dumps_params={'indent': 4})
             

        except ValueError as ve:
            status_code= str(400)
            message= str(ve)            
            return HttpResponse("Error_Code: "+status_code +" Error_Message: "+ message)              
        
    else:
        status_code= str(400)
        return HttpResponse("Error_Code: "+status_code+" Error_Message: The id image and id mask are not the same")

    
    
# Fonctionne pour une image et un mask choisi
def post_radiomics(request, idImage, idMask, idJson):
    image=str(settings.BASE_DIR)+"/app/Storage/image_"+str(idImage)+".nii"     
    mask=str(settings.BASE_DIR)+"/app/Storage/mask_"+str(idMask)+".nii"
    id_img = int(idImage)
    id_mask=int(idMask)
    id_Json=int(idJson)
    
    #On verifie que les images existent: 
    try :
        img_pt=sitk.ReadImage(image)
        img_mask=sitk.ReadImage(mask)    
    except RuntimeError as re:
        status_code=str(400)
        message=str(re)
        print(re)            
        return HttpResponse("Error_Code: "+status_code +" Error_Message: "+ message)

# Conversion mask 4D en mask 3D
    if img_mask.GetDimension()==4:
    
        origin = img_pt.GetOrigin()
        direction = img_pt.GetDirection()
        spacing = img_pt.GetSpacing()

        img_mask_array = sitk.GetArrayFromImage(img_mask)
        mask_3D=img_mask_array[1,:,:,:]
        mask_3D=GetImageFromArray(mask_3D)

        mask_3D.SetOrigin(origin)
        mask_3D.SetSpacing(spacing)
        mask_3D.SetDirection(direction)
#Fin Conversion

    # print(request.body)
    if idImage==id_img and idMask==id_mask and id_mask==id_img and idJson==id_Json and id_img==id_Json:
        try:
        
            pyradiomics_adapter_instance = pyradiomics_adapter()
            # pyradiomics_adapter_instance.set_img()
            # pyradiomics_adapter_instance.set_mask()
            pyradiomics_response = pyradiomics_adapter_instance.calculate(img_pt,mask_3D,idJson)    
            return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder, json_dumps_params={'indent': 4})

        except ValueError as ve:
            status_code= str(400)
            message= str(ve)            
            return HttpResponse("Error_Code: "+status_code +" Error_Message: "+ message)        
        
    else:
        status_code= str(400)
        return HttpResponse("Error_Code: "+status_code+" Error_Message: The id image and id mask are not the same")
    