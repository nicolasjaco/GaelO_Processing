import hashlib
import base64
import os

from django.conf import settings
from django.http import JsonResponse


def handle(request):
    method = request.method
    if(method == 'POST'):
        data = request.read()
        img_id = create_image(data)
        return JsonResponse({'id': img_id})
    if(method == 'GET'):
        id_list = get_image_id()
        return JsonResponse(id_list, safe=False)


def create_image(data: str) -> str:
    """[Store an image with unique ID]

       Content of the POST request

        Create a new instance image with unique ID in HASH  
        Returns: 
        [str]:[id image]
        """
    data_path = settings.STORAGE_DIR
    image_md5 = hashlib.md5(str(data).encode())
    image = base64.b64decode(data)
    image_id = image_md5.hexdigest()
    decode_image = open(data_path+'/image/image_'+image_id+'.nii', 'wb')
    decode_image.write(image)
    decode_image.close()
    return image_id


def get_image_id() -> list:
    """

    Returns:
        [list]: [Return a list with all Image id content in the storage]
    """
    storage_folder = settings.STORAGE_DIR+'/image'
    list_id = []
    for f in os.listdir(storage_folder):
        if os.path.isfile(os.path.join(storage_folder, f)):
            id = f[6:-4]
            list_id.append(id)
    return list_id
