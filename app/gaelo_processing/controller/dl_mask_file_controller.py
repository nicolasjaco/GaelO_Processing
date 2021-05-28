import tempfile

from django.conf import settings
from django.http import HttpResponse

def handle(request,idMask=''):
    method = request.method 
    if(method=='GET'):
        get_mask_file(idMask)
        return HttpResponse(status=200)

def get_mask_file(idMask :int) -> None:
    destination=tempfile.mkdtemp(prefix='mask_nii_')
    print(destination)
    mask=settings.STORAGE_DIR+'/mask/mask_'+str(idMask)+'.nii'
    mask=open(mask,'rb').read()
    file=open(destination+'/mask_'+str(idMask)+'.nii','wb')
    file.write(mask)
    print(file.name)
    # file.close()