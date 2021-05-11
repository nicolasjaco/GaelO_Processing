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
        return create_image(request)

def delete_image(idImage):
    """[Delete the Image]

        Args:
            idImage (int): [Input idImage]
        
        Removes the specified image     
        """       
    os.remove(str(settings.BASE_DIR) +"/app/Storage/image_"+str(idImage)+".nii")

def create_image(request): 
    """[Store an image with unique ID]

       Content of the POST request
        
        Create a new instance image with unique ID    
        """    
    data_path=str(settings.BASE_DIR)+'/app/Storage'   
    data = request.read()    
    image_md5 = hashlib.md5(str(data).encode())
    image=base64.b64decode(data)
    id_img=image_md5.hexdigest()     
    decode_image = open(data_path+'/image_'+id_img+'.nii', 'wb')
    decode_image.write(image)
    decode_image.close()          
    return JsonResponse({'id':image_md5.hexdigest()})
    
