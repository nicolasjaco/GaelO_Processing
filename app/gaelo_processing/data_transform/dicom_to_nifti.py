import tempfile
import shutil
from django.conf import settings

from library_dicom.dicom_processor.model.Series import Series
from ..utips.utips import Utips


class Dicom_To_Nifti:
    def to_nifti(self, folder_path: str):
        path = folder_path
        nifti_temp = tempfile.mkstemp(prefix='nifti_temp')
        Series.__init__(self, path)
        Series.export_nifti(self, file_path=nifti_temp, mask=None)
        shutil.rmtree(path)
