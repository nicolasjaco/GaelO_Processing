from django.http import HttpResponse, JsonResponse, request
from django.conf import settings
import os
import hashlib
import base64

def handle(request, idMask = ''):    
    method = request.method
    if(method == 'DELETE') : 
        delete_mask(idMask)
        return HttpResponse(status=200)   
    if(method=='POST'):
        data = request.read()
        id_mask = create_mask(data)
        return JsonResponse({'id': id_mask})
        
def delete_mask(idMask :int) -> None :
    """[Delete the Mask]

        Args:
            idMask (int): [Input idMask]
        
        Removes the specified mask     
        """       
    os.remove(settings.STORAGE_DIR+"/mask_"+str(idMask)+".nii")

def create_mask(data :str ) -> str:
    data_path=settings.STORAGE_DIR   
    mask_md5 = hashlib.md5(str(data).encode())
    mask=base64.b64decode(data)  
    id_mask=mask_md5.hexdigest()
    decode_mask = open(data_path+'/mask_'+id_mask+'.nii', 'wb')
    decode_mask.write(mask)
    decode_mask.close()          
    return id_mask