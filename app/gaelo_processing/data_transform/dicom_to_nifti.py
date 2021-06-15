import tempfile
import shutil
from django.conf import settings

from dicom_to_cnn.model.reader.Series import Series
from dicom_to_cnn.tools.pre_processing import series
from dicom_to_cnn.model.reader.SeriesCT import SeriesCT
# from dicom_to_cnn.model.reader.SeriesPT import SeriesPT
from ..utips.utips import Utips

class DicomToCnn:
    def to_nifti(self,folder_path: str):
        path = folder_path
        # nifti_temp = tempfile.mkstemp(prefix='nifti_temp')
        nifti=series.get_series_object(path)
        # nifti=nifti.get_numpy_array()
        nifti=nifti.get_series_details()
        print(nifti)
        # print(nifti.export_nifti('C:/Users/Nicolas/Desktop/image.nii'))
        # nifti_str=str(nifti)
        # nifti_str=nifti_str[1:44]
        # if nifti_str=='dicom_to_cnn.model.reader.SeriesCT.SeriesCT':  
        #     nifti=nifti.get_numpy_array()