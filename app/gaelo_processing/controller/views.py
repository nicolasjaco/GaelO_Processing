from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..adapter.pyradiomics_adapter import pyradiomics_adapter
from ..data_object import conversion
import SimpleITK as sitk 
from SimpleITK import GetImageFromArray
import os
import numpy as np
from radiomics import featureextractor
import json
from json import JSONEncoder
from ..data_object.pyradiomics_response import NumpyArrayEncoder
from django.conf import settings
# from jsonschema import SchemaError
from django.core.exceptions import BadRequest
from ..exceptions import custom_exceptions
from django.http import Http404
from django.core import exceptions

#On teste si c est une methode POST ou GET
def handle(request, idImage = '' , idMask = '', idJson=''):
    method = request.method
    if(method == 'GET') : 
        return get_radiomics(request, idImage, idMask, idJson)
    if(method == 'POST') : 
        return post_radiomics(request, idImage, idMask, idJson)

#Pour pouvoir vérifier l'affichage en web mais a del par la suite
def get_radiomics(request, idImage, idMask, idJson):
    image=str(settings.BASE_DIR)+"/app/Storage/image_"+str(idImage)+".nii"     
    mask=str(settings.BASE_DIR)+"/app/Storage/mask_"+str(idMask)+".nii"       
    
    #On verifie que les images existent: 
    try :
        image=sitk.ReadImage(image)
        mask=sitk.ReadImage(mask)   
    
    except RuntimeError as re:        
        return custom_exceptions.handler_404(request, str(re))

    if mask.GetDimension()!=image.GetDimension():
        mask=conversion.convert(image,mask)

    try:      
        pyradiomics_adapter_instance = pyradiomics_adapter()
        # pyradiomics_adapter_instance.set_img()
        # pyradiomics_adapter_instance.set_mask() 
        try:           
            pyradiomics_response = pyradiomics_adapter_instance.calculate(image, mask, idJson)    
            return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder, json_dumps_params={'indent': 4})      

        except FileNotFoundError as fnf:
            return custom_exceptions.handler_404(request, str(fnf))        

    except ValueError as ve:      
        return custom_exceptions.handler_400(request, str(ve))
           
    

def post_radiomics(request, idImage, idMask, idJson):
    """[Trigger pyRadiomics calculation]

        Args:
            idImage (int): [Input idImage]
            idMask (int): [Input idMask]
            idJson(int): [Input idJson]

        Returns:
           JsonResponse: [PyRadiomics results]
            """      
    image=str(settings.BASE_DIR)+"/app/Storage/image_"+str(idImage)+".nii"     
    mask=str(settings.BASE_DIR)+"/app/Storage/mask_"+str(idMask)+".nii"    
    
    #On verifie que les images existent: 
    try :
        image=sitk.ReadImage(image)
        mask=sitk.ReadImage(mask) 

    except RuntimeError as re:        
        return custom_exceptions.handler_404(request, str(re))

    #Si le mask n'est pas de la même dimension que l'image on la convertie
    if mask.GetDimension()!=image.GetDimension():
        mask=conversion.convert(image,mask)

    try:      
        pyradiomics_adapter_instance = pyradiomics_adapter()
        # pyradiomics_adapter_instance.set_img()
        # pyradiomics_adapter_instance.set_mask() 
        try:           
            pyradiomics_response = pyradiomics_adapter_instance.calculate(image, mask, idJson)    
            return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder, json_dumps_params={'indent': 4})      

        except FileNotFoundError as fnf:
            return custom_exceptions.handler_404(request, str(fnf))        

    except ValueError as ve:      
        return custom_exceptions.handler_400(request, str(ve))     