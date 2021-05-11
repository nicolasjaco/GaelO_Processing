from django.shortcuts import render
from django.http import JsonResponse
from ..adapter.pyradiomics_adapter import pyradiomics_adapter
from ..data_object import conversion
import SimpleITK as sitk
from radiomics import featureextractor
import json
from ..data_object.pyradiomics_response import NumpyArrayEncoder
from django.conf import settings
from ..exceptions.gaelo_processor_exeptions import GaelOBadRequestException, GaelONotFoundException
import jsonschema

def handle(request, idImage='', idMask=''):
    method = request.method   
    if(method == 'POST'):
        return post_radiomics(request, idImage, idMask)

def post_radiomics(request, idImage, idMask):
    """
    [Trigger post the radiomics results ]

        Args:
            idImage (int): [Input idImage]
            idMask (int): [Input idMask]
            idJson(int): [Input idJson]

        Returns:
           JsonResponse: [PyRadiomics results]
            """
    image = str(settings.BASE_DIR)+"/app/Storage/image_"+str(idImage)+".nii"
    mask = str(settings.BASE_DIR)+"/app/Storage/mask_"+str(idMask)+".nii"

    # On verifie que les images existent:
    try:
        image = sitk.ReadImage(image)
        mask = sitk.ReadImage(mask)

    except RuntimeError as re:
        raise GaelONotFoundException(str(re))

    # Si le mask n'est pas de la même dimension que l'image on la convertie
    if mask.GetDimension() != image.GetDimension():
        mask = conversion.convert(image, mask)

    try:
        pyradiomics_adapter_instance = pyradiomics_adapter()
        jsonPayload = request.read()      
        pyradiomics_response = pyradiomics_adapter_instance.calculate(image, mask, jsonPayload)       
        return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder, json_dumps_params={'indent': 4})

    except ValueError as ve:        
        raise GaelOBadRequestException(str(ve))
