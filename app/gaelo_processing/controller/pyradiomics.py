from django.http import JsonResponse
from django.conf import settings

import SimpleITK as sitk

from ..data_object.pyradiomics_response import NumpyArrayEncoder
from ..adapter.pyradiomics_adapter import pyradiomics_adapter
from ..exceptions.gaelo_processor_exeptions import GaelOBadRequestException, GaelONotFoundException


def handle(request, idImage='', idMask=''):
    method = request.method
    if(method == 'POST'):
        json_payload = request.read()
        pyradiomics_response = post_radiomics(json_payload, idImage, idMask)
        return JsonResponse(pyradiomics_response.get_dictionary(), NumpyArrayEncoder)


def post_radiomics(json_payload: str, idImage: str, idMask: str) -> JsonResponse:
    """
    [Trigger post the radiomics results ]

        Args:
            idImage (int): [Input idImage]
            idMask (int): [Input idMask]
            idJson(int): [Input idJson]

        Returns:
           JsonResponse: [PyRadiomics results]
    """
    image = settings.STORAGE_DIR+"/image/image_"+idImage+".nii"
    mask = settings.STORAGE_DIR+"/mask/mask_"+idMask+".nii"

    # We check that images are existing in the local storage
    try:
        image = sitk.ReadImage(image)
        mask = sitk.ReadImage(mask)

    except RuntimeError as re:
        raise GaelONotFoundException(str(re))

    try:
        pyradiomics_adapter_instance = pyradiomics_adapter()
        pyradiomics_response = pyradiomics_adapter_instance.calculate(
            image, mask, json_payload)
        return pyradiomics_response

    except ValueError as ve:
        raise GaelOBadRequestException(str(ve))
