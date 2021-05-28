import hashlib
import base64
import os
import json

from django.conf import settings
from django.http import JsonResponse

def handle(request):
    method = request.method    
    if(method=='POST'):  
        data = request.read() 
        img_id = create_image(data)
        return JsonResponse({'id':img_id}) 
    if(method=='GET'):
        id_list= get_image_id()
        return JsonResponse(id_list,safe=False)

def create_image(data :int) -> str : 
    """[Store an image with unique ID]

       Content of the POST request
        
        Create a new instance image with unique ID    
        """    
    data_path=settings.STORAGE_DIR      
    image_md5 = hashlib.md5(str(data).encode())
    image=base64.b64decode(data)
    image_id = image_md5.hexdigest()   
    decode_image = open(data_path+'/image/image_'+image_id+'.nii', 'wb')
    decode_image.write(image)
    decode_image.close()          
    return image_id


def get_image_id():
    storage_folder=settings.STORAGE_DIR+'/image'       
    liste_id=[]    
    for f in os.listdir(storage_folder):
        if os.path.isfile(os.path.join(storage_folder, f)):            
            id=f[6:-4]                      
            liste_id.append(id)                   
    return liste_id