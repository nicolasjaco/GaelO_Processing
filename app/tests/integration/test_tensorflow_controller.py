from django.test import TestCase
import tensorflow
from django.test import Client

from ...gaelo_processing.models.Tensorflow import Tensorflow
from ...gaelo_processing.controller import tensorflow_controller

class MyTest(TestCase):
    def test_predict(self):
        setting = {"id":"2.16.840.1.113669.632.20.870421.10000713812_mip_ct"}
        c=Client()
        response=c.post('/app/model/aquisition_field_model/inference',setting,content_type='application/json')
        self.assertTrue(response.status_code == 200)
        print('test predict for tensorflow validate')
        # test_tsflow=Tensorflow()
        # result=test_tsflow.predict('aquisition_field_model', 1)
        # print('test tensorflow predict validate')