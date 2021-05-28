import hashlib
import base64
import os

from django.conf import settings
from django.http import JsonResponse

def handle(request):    
    method = request.method  
    if(method=='POST'):
        data = request.read()
        id_mask = create_mask(data)
        return JsonResponse({'id': id_mask})
    if(method=='GET'):
        id_list= get_mask_id()
        return JsonResponse(id_list,safe=False)

def create_mask(data :str ) -> str:
    data_path=settings.STORAGE_DIR   
    mask_md5 = hashlib.md5(str(data).encode())
    mask=base64.b64decode(data)  
    id_mask=mask_md5.hexdigest()
    decode_mask = open(data_path+'/mask/mask_'+id_mask+'.nii', 'wb')
    decode_mask.write(mask)
    decode_mask.close()          
    return id_mask

def get_mask_id():
    storage_folder=settings.STORAGE_DIR+'/image'       
    liste_id=[] 
    for file in os.listdir(storage_folder):
        if os.path.isfile(os.path.join(storage_folder, file)):            
            id=file[5:-4]                      
            liste_id.append(id)               
    return liste_id