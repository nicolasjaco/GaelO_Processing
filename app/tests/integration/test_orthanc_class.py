from django.test import TestCase

from ...gaelo_processing.models.orthanc import Orthanc


class test_orthanc_class(TestCase):
    def test_get_zip_from_orthanc(self):
        ortanc_instance = Orthanc()
        zip_path = ortanc_instance.get_zip_from_orthanc(
            "3a84b7f7-d0c66087-d70b292e-0c585356-56b6ccb3")
        print('test get_zip_from_orthanc validate')