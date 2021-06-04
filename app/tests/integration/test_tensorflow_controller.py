from django.test import TestCase
from django.test import Client


class MyTest(TestCase):
    def test_predict(self):
        setting = {"id": "2.16.840.1.113669.632.20.870421.10000713812_mip_ct"}
        c = Client()
        response = c.post('/app/models/aquisition_field_model/inference',
                          setting, content_type='application/json')
        self.assertTrue(response.status_code == 200)
        print('test predict for tensorflow validate')
