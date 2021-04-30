import os
import SimpleITK as sitk 
from SimpleITK import GetImageFromArray
import json
from radiomics import featureextractor,firstorder
from datetime import date,datetime
import hashlib
from django.http import HttpResponse, JsonResponse

# data_path='D:/Code/Rest_Radiomics/app/Storage'
# def create_img_mask(request,idImage,idMask):
#     id_img=str(idImage)
#     id_mask=str(idMask)
#     md5_img=hashlib.md5(id_img.encode())
#     md5_mask=hashlib.md5(id_mask.encode())

#     # img=sitk.ReadImage("C:/Users/Nicolas/Desktop/Img_Stage/image_1c.nii") 
    
#     # sitk.WriteImage(image,"D:/Code/Rest_Radiomics/app/Storage/image_"+md5_img.hexdigest()+".nii")
#     # sitk.WriteImage(mask,"D:/Code/Rest_Radiomics/app/Storage/mask_"+md5_mask.hexdigest()+".nii")
#     return HttpResponse("Image and Mask create")