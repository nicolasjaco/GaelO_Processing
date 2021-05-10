from radiomics import featureextractor
import SimpleITK as sitk
from SimpleITK import GetImageFromArray
import os
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..data_object.pyradiomics_response import pyradiomics_response
import json
import jsonschema
from django.core.exceptions import ValidationError
from ..exceptions import custom_exceptions

class pyradiomics_adapter:
    
    def calculate(self, image : sitk.Image, mask : sitk.Image, JSON:json) -> pyradiomics_response :
        """[Trigger pyRadiomics calculation]

        Args:
            image (sitk.Image): [Input Image]
            mask (sitk.Image): [Input mask]

        Returns:
            pyradiomics_response: [Handler for pyRadiomics reponse]
        """       
        dataDir='C:/Users/Nicolas/Desktop/' 
        id_json=str(JSON)        
        params = os.path.join(dataDir,"params_image_"+id_json+".json")       
        with open(params) as data:
            params_dict = json.load(data)
            params_str = json.dumps(params_dict)     
        extractor = featureextractor.RadiomicsFeatureExtractor() 
     
        extractor.loadJSONParams(params_str) 
       
        results=extractor.execute(image,mask)
        return pyradiomics_response(results)   

     
        
        

            