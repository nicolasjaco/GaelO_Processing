import tempfile

from django.conf import settings
from django.http import HttpResponse

def handle(request,idImage=''):
    method = request.method 
    if(method=='GET'):
        get_image_file(idImage)
        return HttpResponse(status=200)

def get_image_file(idImage :int) -> None:
    destination=tempfile.mkdtemp(prefix='image_nii_')
    print(destination)
    image=settings.STORAGE_DIR+'/image/image_'+str(idImage)+'.nii'
    image=open(image,'rb').read()
    file=open(destination+'/image_'+str(idImage)+'.nii','wb')
    file.write(image)
    print(file.name)
    # file.close()
   
    
    