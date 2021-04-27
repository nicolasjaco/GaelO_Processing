from radiomics import featureextractor
import SimpleITK as sitk
from SimpleITK import GetImageFromArray
import os
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from ..data_object.pyradiomics_response import pyradiomics_response

class pyradiomics_adapter:


    
    def calculate(self, image : sitk.Image, mask : sitk.Image ) -> pyradiomics_response :
        """[Trigger pyRadiomics calculation]

        Args:
            image (sitk.Image): [Input Image]
            mask (sitk.Image): [Input mask]

        Returns:
            pyradiomics_response: [Handler for pyRadiomics reponse]
        """

        extractor = featureextractor.RadiomicsFeatureExtractor()
        results=extractor.execute(image,mask)       
        return pyradiomics_response(results)
