import base64

from django.test import TestCase
from django.test import Client
from django.conf import settings



class MyTest(TestCase):  

    def test_create_mask(self):
        data_path = settings.STORAGE_DIR+"/mask/mask_8.nii"
        data = open(data_path, "rb").read()
        encoded = base64.b64encode(data)
        c = Client()
        response = c.post('/app/mask', data=encoded.decode(),content_type='image/nii')
        self.assertTrue(response.status_code == 200)
        print('validate')

    def test_get_id(self):
        c=Client()
        response=c.get('/app/mask')
        self.assertTrue(response.status_code == 200)
        print('validate')