from django.urls import path
from django.conf.urls import handler404
from .gaelo_processing.controller import views
from .gaelo_processing.controller import image_controller
from .gaelo_processing.controller import mask_controller
from .gaelo_processing.exceptions import custom_exceptions
from django.conf.urls import handler404, handler500, handler403, handler400, handler500

handler404=custom_exceptions.handler_404
handler400=custom_exceptions.handler_400
handler500=custom_exceptions.handler_500

urlpatterns = [
    path('radiomics/image/<str:idImage>/mask/<str:idMask>/json/<int:idJson>',views.handle,name='post_radiomics'),
    path('image/<str:idImage>',image_controller.handle,name='delete_image'),
    path('mask/<str:idMask>',mask_controller.handle,name='delete_mask'),
    path('image',image_controller.handle,name='create_image'),
    path('mask',mask_controller.handle,name='create_mask'),
    
]
