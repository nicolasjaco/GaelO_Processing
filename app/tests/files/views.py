from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .gaelo_processing.adapter.pyradiomics_adapter import pyradiomics_adapter
import SimpleITK as sitk 
from SimpleITK import GetImageFromArray
import os
import numpy as np
from radiomics import featureextractor
import json
from json import JSONEncoder
from .gaelo_processing.data_object.pyradiomics_response import NumpyArrayEncoder

data_path='D:/Code/Rest_Radiomics/app/tests/files'

# c=os.listdir('D:/Code/Rest_Radiomics/app/tests/files')
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

# Fonctionne pour n'importe quelle image et n'importe quel mask
def get_radiomics(request):
    img_n1_load = os.path.join(data_path, 'image_1.nii')  
    img_pt=sitk.ReadImage(img_n1_load)

    mask_n1_load =os.path.join(data_path, 'mask_1.nii')
    img_mask=sitk.ReadImage(mask_n1_load)
    origin = img_pt.GetOrigin()
    direction = img_pt.GetDirection()
    spacing = img_pt.GetSpacing()

    img_mask1_array = sitk.GetArrayFromImage(img_mask)
    mask_3D=img_mask1_array[1,:,:,:]
    mask_3D=GetImageFromArray(mask_3D)

    mask_3D.SetOrigin(origin)
    mask_3D.SetSpacing(spacing)
    mask_3D.SetDirection(direction)
    pyradiomics_adapter_instance = pyradiomics_adapter()
    # pyradiomics_adapter_instance.set_img()
    # pyradiomics_adapter_instance.set_mask()    
    pyradiomics_response = pyradiomics_adapter_instance.calculate(img_pt,mask_3D)
    return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder, json_dumps_params={'indent': 4})

# Fonctionne pour une image et un mask choisi

def post_test(request, idImage, idMask):
    image=os.path.join(data_path,"image_"+str(idImage)+".nii")  
    mask=os.path.join(data_path,"mask_"+str(idMask)+".nii") 
    id_img = int(idImage)
    id_mask=int(idMask)
    img_pt=sitk.ReadImage(image)
    img_mask=sitk.ReadImage(mask)
# Conversion
    if img_mask.GetDimension()==4:
    
        origin = img_pt.GetOrigin()
        direction = img_pt.GetDirection()
        spacing = img_pt.GetSpacing()

        img_mask1_array = sitk.GetArrayFromImage(img_mask)
        mask_3D=img_mask1_array[1,:,:,:]
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
            # os.remove(data_path+"/image_"+str(idImage)+".nii")
            # os.remove(data_path+"/mask_"+str(idMask)+".nii")       
            return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder, json_dumps_params={'indent': 4})
        
        else:
            return HttpResponse("L id mask/img ne correspond pas ou est inexistant")

    except ValueError as ve:
        status_code= str(400)
        message= str(ve)
        return HttpResponse("Error_Code: "+status_code +" Message_Error: "+ message+" please change label.")
        
