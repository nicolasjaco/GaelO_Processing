from django.http import HttpResponse, JsonResponse
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
        return create_mask(request)
        
def delete_mask(idMask):
    """[Delete the Mask]

        Args:
            idMask (int): [Input idMask]
        
        Removes the specified mask     
        """       
    os.remove(str(settings.BASE_DIR)+"/app/Storage/mask_"+str(idMask)+".nii")

def create_mask(request):
    data_path=str(settings.BASE_DIR)+'/app/Storage'   
    data = request.read()
    mask_md5 = hashlib.md5(str(data).encode())
    mask=base64.b64decode(data)  
    id_mask=mask_md5.hexdigest()
    decode_mask = open(data_path+'/mask_'+id_mask+'.nii', 'wb')
    decode_mask.write(mask)
    decode_mask.close()          
    return JsonResponse({'id': mask_md5.hexdigest()})