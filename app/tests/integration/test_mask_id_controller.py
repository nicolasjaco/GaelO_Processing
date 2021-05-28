from django.test import TestCase
from django.test import Client
from django.conf import settings

class MyTest(TestCase):

    def test_delete_image(self):
        image = open(settings.STORAGE_DIR+'/mask/mask_3.nii', 'wb')
        image.close()
        c = Client()
        response = c.delete('/app/mask/3')
        self.assertTrue(response.status_code == 200)
        print('validate')

    def test_get_metadata(self):
        c=Client()
        response=c.get('/app/mask/8',content_type='application/json')
        print(response.content)
        self.assertTrue(response.status_code == 200)
        print('validate')