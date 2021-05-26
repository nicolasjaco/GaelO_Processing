import os


from django.http import HttpResponse, JsonResponse, request
from django.conf import settings

def handle(request, idMask = ''):    
    method = request.method
    if(method == 'DELETE') : 
        delete_mask(idMask)
        return HttpResponse(status=200)   
    
        
def delete_mask(idMask :int) -> None :
    """[Delete the Mask]

        Args:
            idMask (int): [Input idMask]
        
        Removes the specified mask     
        """       
    os.remove(settings.STORAGE_DIR+"/mask/mask_"+str(idMask)+".nii")

