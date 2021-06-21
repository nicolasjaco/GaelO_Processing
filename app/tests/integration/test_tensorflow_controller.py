from django.test import TestCase
from django.test import Client


class test_tensorflow_controller(TestCase):
    def test_predict(self):
        setting = {"id": "9d1f6b1606e0b318a8dff0928564ccc4"}
        c = Client()
        response = c.post('/app/models/aquisition_field_model/inference',
                          setting, content_type='application/json')
        self.assertTrue(response.status_code == 200)
        print('test predict for tensorflow validate')
