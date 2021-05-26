from ..data_object.pyradiomics_response import pyradiomics_response
from ..data_object.pyradiomics_response import NumpyArrayEncoder

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
        return JsonResponse(metadata.get_metadata_dictionary(),NumpyArrayEncoder)


def delete_image(idImage :int) -> None :
    """[Delete the Image]

        Args:
            idImage (int): [Input idImage]
        
        Removes the specified image     
        """       
    os.remove(settings.STORAGE_DIR+"/image/image_"+str(idImage)+".nii")

def get_metadata(idImage :int) :
    image =settings.STORAGE_DIR+"/image/image_"+str(idImage)+".nii"
    results=sitk.ReadImage(image)    
    return pyradiomics_response(results)



