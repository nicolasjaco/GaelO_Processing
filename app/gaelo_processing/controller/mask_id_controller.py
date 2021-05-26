from ..data_object.pyradiomics_response import pyradiomics_response
from ..data_object.pyradiomics_response import NumpyArrayEncoder

import os
import SimpleITK as sitk

from django.http import HttpResponse, JsonResponse
from django.conf import settings

def handle(request, idMask = ''):    
    method = request.method
    if(method == 'DELETE') : 
        delete_mask(idMask)
        return HttpResponse(status=200)
    if(method=='GET'):
        metadata=get_metadata(idMask)        
        return JsonResponse(metadata.get_metadata_dictionary(),NumpyArrayEncoder)   
    
        
def delete_mask(idMask :int) -> None :
    """[Delete the Mask]

        Args:
            idMask (int): [Input idMask]
        
        Removes the specified mask     
        """       
    os.remove(settings.STORAGE_DIR+"/mask/mask_"+str(idMask)+".nii")


def get_metadata(idMask :int) :
    image =settings.STORAGE_DIR+"/image/image_"+str(idMask)+".nii"
    results=sitk.ReadImage(image)    
    return pyradiomics_response(results)

