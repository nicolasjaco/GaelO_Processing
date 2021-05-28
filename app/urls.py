from django.urls import path

from .gaelo_processing.controller import pyradiomics
from .gaelo_processing.controller import image_controller
from .gaelo_processing.controller import mask_controller
from .gaelo_processing.controller import image_id_controller
from .gaelo_processing.controller import mask_id_controller
from .gaelo_processing.controller import dl_image_file_controller
from .gaelo_processing.controller import dl_mask_file_controller
from .gaelo_processing.controller import tensorflow_controller

urlpatterns = [
    path('radiomics/image/<str:idImage>/mask/<str:idMask>',pyradiomics.handle,name='post_radiomics'),
    path('image/<str:idImage>',image_id_controller.handle,name='image_id_controller'),
    path('mask/<str:idMask>',mask_id_controller.handle,name='mask_id_controller'),
    path('image',image_controller.handle,name='image'),
    path('mask',mask_controller.handle,name='mask'),
    path('image/<str:idImage>/file',dl_image_file_controller.handle,name='dl_image_file'),
    path('mask/<str:idMask>/file',dl_mask_file_controller.handle,name='dl_mask_file'),   
    path('model/<str:model_name>/inference', tensorflow_controller.handle,name='get_inference'),
    # path('model/<str:model_name>'),         
]