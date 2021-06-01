from ..data_object.pyradiomics_response import NumpyArrayEncoder
from ..models.SitkImage import get_metadata_dictionary

import os
import SimpleITK as sitk

from django.http import HttpResponse, JsonResponse
from django.conf import settings

def handle(request, idImage = ''):
    method = request.method
    if(method == 'DELETE') : 
        delete_image(idImage)
        return HttpResponse(status=200)
    if(method=='GET'):
        metadata=get_metadata(idImage)        
        return JsonResponse(metadata,NumpyArrayEncoder)

def delete_image(idImage :str) -> None :
    """[Delete the Image]

        Args:
            idImage (str): [Input idImage]
        
        Removes the specified image     
        """       
    os.remove(settings.STORAGE_DIR+"/image/image_"+idImage+".nii")

def get_metadata(idImage :str) ->dict:
    """[Get the metadata from an image]

    Args:
        idImage (str): [Input image]

    Returns:
        dict: [return formated dictionary ready ready to be sent as a JSON]
    """

    path =settings.STORAGE_DIR+"/image/image_"+idImage+".nii"
    image=sitk.ReadImage(path)    
    return get_metadata_dictionary(image)



