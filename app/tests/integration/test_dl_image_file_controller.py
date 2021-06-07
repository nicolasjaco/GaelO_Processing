from django.test import TestCase
from django.test import Client

class test_dl_file_image_controller(TestCase):

    def test_download_image_file(self):
        c=Client()
        response=c.get('/app/images/8/file')
        self.assertTrue(response.status_code == 200)     
        print('test dl_image_file_controller validate')
        