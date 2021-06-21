from django.test import TestCase

from ...gaelo_processing.data_transform.dicom_to_nifti import DicomToCnn

class test_dicom_to_cnn(TestCase):
    def test_to_nifti(self):
        DicomToCnn.to_nifti(self,'C:/Users/Nicolas/AppData/Local/Temp/gaelo_pross_unzip_jz60e_9p')
        print('test dicom-to-cnn validate')

    def test_to_2D(self):
        DicomToCnn.to_2D(self,'9d1f6b1606e0b318a8dff0928564ccc4')
        print('test dicom-to-cnn validate')