from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os
import hashlib
import base64

def handle(request, idImage = ''):
    method = request.method
    if(method == 'DELETE') : 
        delete_image(idImage)
        return HttpResponse(status=200)
    if(method=='POST'):  
        data = request.read() 
        img_id = create_image(data)
        return JsonResponse({'id':img_id}) 

def delete_image(idImage :int) -> None :
    """[Delete the Image]

        Args:
            idImage (int): [Input idImage]
        
        Removes the specified image     
        """       
    os.remove(settings.STORAGE_DIR+"/image_"+str(idImage)+".nii")

def create_image(data :int) -> str : 
    """[Store an image with unique ID]

       Content of the POST request
        
        Create a new instance image with unique ID    
        """    
    data_path=settings.STORAGE_DIR      
    image_md5 = hashlib.md5(str(data).encode())
    image=base64.b64decode(data)
    image_id = image_md5.hexdigest()   
    decode_image = open(data_path+'/image_'+image_id+'.nii', 'wb')
    decode_image.write(image)
    decode_image.close()          
    return image_id
    
