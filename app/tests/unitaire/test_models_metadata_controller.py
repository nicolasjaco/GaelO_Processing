from django.test import TestCase

from ...gaelo_processing.controller import models_metadata_controller


class MyTest(TestCase):

    def test_get_metadata(self):
        data = models_metadata_controller.get_metadata(
            'aquisition_field_model')
        print(data)
        print('test_models_metadata validate')
