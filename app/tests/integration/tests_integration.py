from django.test import TestCase
from django.test import Client


class MyTest(TestCase):
    def test_get_route(self):
        c = Client()
        response = c.get('/app/test')
        self.assertTrue(response.status_code == 200)

    def test_post(self):
        c = Client()

        settings = { "settings": {
            "minimumROIDimensions": 1,
            "minimumROISize": 0,
            "geometryTolerance": 0.5,
            "correctMask": False,
            "additionalInfo": True,
            "label": 3,
            "label_channel": 0,
            "binWidth": 3.5,
            "binCount": 5,
            "normalize": True,
            "normalizeScale": 1.5,
            "removeOutliers": 0,

            }
        }
        print(type(settings))

        response = c.post('/app/test', settings, content_type='application/json')
        print(response.content)
        self.assertTrue(response.status_code == 200)
