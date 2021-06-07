from django.test import TestCase
from django.test import Client
from django.conf import settings


class test_mask_id_controller(TestCase):

    def test_delete_mask(self):
        image = open(settings.STORAGE_DIR+'/mask/mask_3.nii', 'wb')
        image.close()
        c = Client()
        response = c.delete('/app/masks/3')
        self.assertTrue(response.status_code == 200)
        print('test delete_mask validate')

    def test_get_metadata(self):
        c = Client()
        response = c.get('/app/masks/8', content_type='application/json')
        self.assertTrue(response.status_code == 200)
        print('test get metadata for mask validate')
