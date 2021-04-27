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

data_path='C:/Users/Nicolas/Desktop/Img_Stage/'

img_n1_load = os.path.join(data_path, 'img2_nifti_PT.nii')  
img_pt=sitk.ReadImage(img_n1_load)

mask_n1_load =os.path.join(data_path, 'img2_nifti_mask.nii')
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


def get_radiomics(request):
    pyradiomics_adapter_instance = pyradiomics_adapter()
    # pyradiomics_adapter_instance.set_img()
    # pyradiomics_adapter_instance.set_mask()
    pyradiomics_response = pyradiomics_adapter_instance.calculate(img_pt,mask_3D)
    return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder)
    