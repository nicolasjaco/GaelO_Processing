from django.test import TestCase
from django.test import Client


class MyTest(TestCase):
    def test_models_list(self):
        c=Client()
        response=c.get('/app/models',content_type='application/json')
        self.assertTrue(response.status_code == 200)
        print('test models_list validate')