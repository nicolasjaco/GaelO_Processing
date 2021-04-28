from django.urls import path

from . import views

urlpatterns = [
    path('test', views.test, name='get_radiomics'),
    path('test/image/<int:idImage>/mask/<int:idMask>',views.post_test,name='post_test'),
]