from django.urls import path

from .gaelo_processing.controller import views
from .gaelo_processing.controller import image_controller
from .gaelo_processing.controller import mask_controller

urlpatterns = [
    # path('radiomics', views.test, name='get_radiomics'),
    path('radiomics/image/<int:idImage>/mask/<int:idMask>',views.post_radiomics,name='post_radiomics'),
    path('image/<int:idImage>',image_controller.handle,name='delete_image'),
    path('mask/<int:idMask>',mask_controller.handle,name='delete_mask'),
]
