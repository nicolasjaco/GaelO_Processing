from django.test import TestCase
from django.test import Client
from django.conf import settings

class MyTest(TestCase):

    def test_download_image_file(self):
        c=Client()
        response=c.get('/app/image/8/file')
        self.assertTrue(response.status_code == 200)     
        print('test dl_image_file_controller validate')