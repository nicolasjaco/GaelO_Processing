from radiomics import featureextractor,firstorder
import SimpleITK as sitk
from SimpleITK import GetImageFromArray
import os
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from ..data_object.pyradiomics_response import pyradiomics_response
import json


class pyradiomics_adapter:

    
    def calculate(self, image : sitk.Image, mask : sitk.Image) -> pyradiomics_response :
        """[Trigger pyRadiomics calculation]

        Args:
            image (sitk.Image): [Input Image]
            mask (sitk.Image): [Input mask]

        Returns:
            pyradiomics_response: [Handler for pyRadiomics reponse]
        """
        dataDir='C:/Users/Nicolas/Desktop/' 
        
        params = os.path.join(dataDir,"params_image_2.json")
        with open(params) as data:
           params_dict = json.load(data)
           params_str = json.dumps(params_dict)        
        # params = os.path.join(dataDir,"params.yml")  
        extractor = featureextractor.RadiomicsFeatureExtractor()
        extractor.loadJSONParams(params_str)
        # extractor.loadParams(params)
        results=extractor.execute(image,mask)       
        return pyradiomics_response(results)