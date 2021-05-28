import tempfile
import os

from django.conf import settings
from django.http import HttpResponse
from django.http.response import Http404

def handle(request,idImage=''):
    method = request.method 
    if(method=='GET'):
        return download_image_file(idImage)

def download_image_file(idImage :int) -> None:
    image_path=settings.STORAGE_DIR+'/image/image_'+str(idImage)+'.nii'
    if os.path.exists(image_path):
        with open(image_path, 'rb') as image:
            return HttpResponse(image, content_type="image/nii")
    else: raise Http404