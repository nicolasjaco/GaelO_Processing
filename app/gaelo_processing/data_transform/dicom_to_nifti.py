from library_dicom.dicom_processor.model.Series import Series
from ..utips.utips import Utips
from django.conf import settings
import tempfile


class Dicom_To_Nifti:       
        def to_nifti(folder_path):
                path=folder_path               
                nifti_temp=tempfile.mkdtemp(prefix='nifti_temp')
                Series.__init__(path)
                Series.export_nifti(file_path=nifti_temp,mode='pet',mask=None)
                # shutil.rmtree(path)