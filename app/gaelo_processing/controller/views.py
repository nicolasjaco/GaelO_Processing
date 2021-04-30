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
import ntpath
import posixpath


# c=os.listdir('D:/Code/Rest_Radiomics/app/Storage')
# image=c[0]
# mask=c[1]
# id_img = int(image[6])
# id_mask=int(mask[5])

#On teste si c est une methode POST ou GET
def test(request, idImage = '' , idMask = ''):
    method = request.method
    if(method == 'GET') : 
        return get_radiomics(request)
    if(method == 'POST') : 
        return post_test(request, idImage, idMask)

# Fonctionne pour une image et un mask choisi

def post_radiomics(request, idImage, idMask):
    image=str(settings.BASE_DIR)+"/app/Storage/image_"+str(idImage)+".nii"     
    mask=str(settings.BASE_DIR)+"/app/Storage/mask_"+str(idMask)+".nii"
    id_img = int(idImage)
    id_mask=int(idMask)
    img_pt=sitk.ReadImage(image)
    img_mask=sitk.ReadImage(mask)

# Conversion
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
    try:
        if idImage==id_img and idMask==id_mask and id_mask==id_img:
            pyradiomics_adapter_instance = pyradiomics_adapter()
            # pyradiomics_adapter_instance.set_img()
            # pyradiomics_adapter_instance.set_mask()
            pyradiomics_response = pyradiomics_adapter_instance.calculate(img_pt,mask_3D)               
            return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder, json_dumps_params={'indent': 4})
        
        else:
            return HttpResponse("The id mask/image are not the same or doesn't exist.")

    except ValueError as ve:
        status_code= str(400)
        message= str(ve)
        return HttpResponse("Error_Code: "+status_code +" Message_Error: "+ message+" please change label.")
        
