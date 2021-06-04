import SimpleITK as sitk
import json

from django.test import TestCase
from django.conf import settings


from ...gaelo_processing.adapter.pyradiomics_adapter import pyradiomics_adapter


class MyTest(TestCase):

    def test_pyrad(self):
        setting = {
            "setting": {
                "minimumROIDimensions": 2,
                "minimumROISize": 1,
                "binWidth": 3.5,
                "normalize": False,
                "force2D": False,
                "label": 1,
                "geometryTolerance": 0.5,
                "correctMask": False,
                "additionalInfo": True,
                "label_channel": 0,
                "binCount": 5,
                "normalizeScale": 1.5,
                "removeOutliers": 1,
                "resampledPixelSpacing": [1, 2, 3],
                "interpolator": "sitkLinear",
                "padDistance": 0,
                "resegmentMode": "absolute",
                "resegmentShape": True
            }
        }

        img_load = str(settings.BASE_DIR) + '/app/storage/image/image_8.nii'
        img_pt = sitk.ReadImage(img_load)
        mask_load = str(settings.BASE_DIR) + '/app/storage/mask/mask_8.nii'
        img_mask = sitk.ReadImage(mask_load)
        pyradiomics_adapter_instance = pyradiomics_adapter()
        self.assertTrue(pyradiomics_adapter_instance.calculate(
            img_pt, img_mask, json.dumps(setting)) != None)
        print('test pyrad validate')
