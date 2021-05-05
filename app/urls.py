from django.urls import path

from .gaelo_processing.controller import views
from .gaelo_processing.controller import image_controller
from .gaelo_processing.controller import mask_controller

urlpatterns = [
    # path('radiomics', views.test, name='get_radiomics'),
    path('radiomics/image/<str:idImage>/mask/<str:idMask>/json/<int:idJson>',views.handle,name='post_radiomics'),
    path('image/<str:idImage>',image_controller.handle,name='delete_image'),
    path('mask/<str:idMask>',mask_controller.handle,name='delete_mask'),
    path('image',image_controller.handle,name='create_image'),
    path('mask',mask_controller.handle,name='create_mask'),
]
