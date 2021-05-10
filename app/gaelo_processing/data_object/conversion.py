from django.conf import settings
import SimpleITK as sitk 
from SimpleITK import GetImageFromArray, GetArrayFromImage
import os
import numpy as np
from django.http import HttpResponse, JsonResponse

def convert(image:sitk.Image, mask:sitk.Image): 
    """[Resize Fuction]

        Args:
            image (sitk.Image): [Input Image]
            mask (sitk.Image): [Input mask]

        Returns:
            mask_3D: [Converting a 4D mask to a 3D mask]
        """         
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

def convert_2(image:sitk.Image, mask:sitk.Image):
    extract = sitk.ExtractImageFilter()
    mask_array=GetArrayFromImage(mask)


    mask_size = list(mask.GetSize())
    mask_size[-1] = 0  # Setting the size to 0 collapses this dimension
    mask_start = [0] * len(mask_size)  # extract the entire image, starting at [0, 0, 0, ...]

    extract.SetSize(tuple(mask_size))

    masks = []
    for ma_idx in range(mask.GetSize()[-1]):
      mask_start[-1] = ma_idx
      extract.SetIndex(tuple(mask_start))
      masks.append(extract.Execute(mask))

    composer = sitk.ComposeImageFilter()
    new_mask = composer.Execute(masks)

    return new_mask
