import os

from django.conf import settings
from django.http import HttpResponse,Http404

def handle(request,idMask=''):
    method = request.method 
    if(method=='GET'):
        get_mask_file(idMask)
        return HttpResponse(status=200)

def get_mask_file(idMask :str) -> None:
    """[Download the mask file]

    Args:
        idMask (str): [Input mask]

    Raises:
        Http404: [If file not found raise 404 error]

    Returns:
        [NONE]
    """
    mask_path=settings.STORAGE_DIR+'/mask/mask_'+idMask+'.nii'
    if os.path.exists(mask_path):
        with open(mask_path, 'rb') as mask:
            return HttpResponse(mask, content_type="image/nii")
    else: raise Http404
   