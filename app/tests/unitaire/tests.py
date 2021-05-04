from django.test import TestCase
import unittest
from ...gaelo_processing.adapter.pyradiomics_adapter import pyradiomics_adapter
import SimpleITK as sitk 
from SimpleITK import GetImageFromArray
import os
import numpy as np
from django.conf import settings

class MyTest(TestCase):    

    def test_pyrad(self):
        

        img_load = str(settings.BASE_DIR) + '/app/Storage/image_1.nii'
        img_pt=sitk.ReadImage(img_load)

        mask_load =str(settings.BASE_DIR) + '/app/Storage/mask_1.nii'
        img_mask=sitk.ReadImage(mask_load)
        origin = img_pt.GetOrigin()
        direction = img_pt.GetDirection()
        spacing = img_pt.GetSpacing()

        img_mask_array = sitk.GetArrayFromImage(img_mask)
        mask_3D=img_mask_array[1,:,:,:]
        mask_3D=GetImageFromArray(mask_3D)

        mask_3D.SetOrigin(origin)
        mask_3D.SetSpacing(spacing)
        mask_3D.SetDirection(direction)
        self.assertTrue(pyradiomics_adapter.calculate(self,img_pt,mask_3D)!=None)
    


       
