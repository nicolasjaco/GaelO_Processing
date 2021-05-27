from django.test import TestCase
from django.test import Client
from django.conf import settings



class MyTest(TestCase):

    def test_dl_image_file_controller(self):
        c=Client()
        response=c.get('app/image/8/file')
        print(response.status_code)
        self.assertTrue(response.status_code == 200)     
        print('validate')