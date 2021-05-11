from django.test import TestCase
from django.test import Client
from django.conf import settings
import base64
import SimpleITK as sitk


class MyTest(TestCase):

    def test_post(self):
        c = Client()
        setting = {"setting": {
            "minimumROIDimensions": 2,
            "minimumROISize": 1,
            "binWidth": 3.5,
            "normalize": False,
            "force2D": True,
            "label": 2,
            "geometryTolerance": 0.5,
            "correctMask": False,
            "additionalInfo": True,
            "label_channel": 0,
            "binCount": 5,
            "normalizeScale": 1.5,
            "removeOutliers": 1,
            "resampledPixelSpacing": [1, 2, 3],
            "interpolator": "sitkLinear"
        }
        }
        response = c.post('/app/radiomics/image/2/mask/2',setting, content_type='application/json')
        self.assertTrue(response.status_code == 200)

    def test_delete_image(self):
        image = open(str(settings.BASE_DIR)+'/app/Storage/image_3.nii', 'wb')
        image.close()
        c = Client()
        response = c.delete('/app/image/3')
        self.assertTrue(response.status_code == 200)

    def test_delete_mask(self):
        mask = open(str(settings.BASE_DIR)+'/app/Storage/mask_3.nii', 'wb')
        mask.close()
        c = Client()
        response = c.delete('/app/mask/3')
        self.assertTrue(response.status_code == 200)

    def test_create_and_delete_image(self):
        data_path = str(settings.BASE_DIR)+"/app/Storage/image_1.nii"
        data = open(data_path, "rb").read()
        encoded = base64.b64encode(data)
        c = Client()
        response = c.post('/app/image', data=encoded.decode(),content_type='image/nii')
        self.assertTrue(response.status_code == 200)

    def test_create_and_delete_mask(self):
        data_path = str(settings.BASE_DIR)+"/app/Storage/mask_1.nii"
        data = open(data_path, "rb").read()
        encoded = base64.b64encode(data)
        c = Client()
        response = c.post('/app/mask', data=encoded.decode(),content_type='image/nii')
        self.assertTrue(response.status_code == 200)
