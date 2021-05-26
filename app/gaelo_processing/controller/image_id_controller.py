from ..data_object.pyradiomics_response import pyradiomics_response

import os
import nibabel as nib

from django.http import HttpResponse, JsonResponse
from django.conf import settings

def handle(request, idImage = ''):
    method = request.method
    if(method == 'DELETE') : 
        delete_image(idImage)
        return HttpResponse(status=200)
    if(method=='GET'):
        return JsonResponse


def delete_image(idImage :int) -> None :
    """[Delete the Image]

        Args:
            idImage (int): [Input idImage]
        
        Removes the specified image     
        """       
    os.remove(settings.STORAGE_DIR+"/image/image_"+str(idImage)+".nii")

def get_metadata(idImage :int) :
    image = 'C:/Users/Nicolas/Desktop/Img_Stage/image_'+str(idImage)+'.nii'
    image = nib.load(image)
    image_header = image.header
    return pyradiomics_response(image_header)
