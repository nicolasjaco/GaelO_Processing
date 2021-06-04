from django.test import TestCase
from django.test import Client


class MyTest(TestCase):
    def test_get_zip_dicom(self):
        c = Client()
        zip_file = 'orthanc.zip'
        zip_file = open(zip_file, 'rb')
        zip_file = zip_file.read()
        response = c.post('/app/dicom', zip_file,
                          content_type='application/zip')
        self.assertTrue(response.status_code == 200)
        print('test get_zip_dicom validate')
