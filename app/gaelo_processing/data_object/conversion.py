from django.conf import settings
import SimpleITK as sitk 
from SimpleITK import GetImageFromArray
import os
import numpy as np
from django.http import HttpResponse, JsonResponse

def convert(image:sitk.Image, mask:sitk.Image):   
    if mask.GetDimension()==4:

        origin = image.GetOrigin()
        direction = image.GetDirection()
        spacing = image.GetSpacing()

        img_mask_array = sitk.GetArrayFromImage(mask)
        mask_3D=img_mask_array[1,:,:,:]
        mask_3D=GetImageFromArray(mask_3D)

        mask_3D.SetOrigin(origin)
        mask_3D.SetSpacing(spacing)
        mask_3D.SetDirection(direction)
    
    return mask_3D

