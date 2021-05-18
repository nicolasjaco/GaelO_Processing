from library_dicom.dicom_processor.model.Series import Series
from ..utips.utips import Utips
from django.conf import settings
import tempfile
class Dicom_To_Nifti:       
        def to_nifti(folder_path):
                path=folder_path
                instance_dicom=Series()
                nifti_temp=tempfile.mkdtemp(prefix='nifti_temp')
                instance_dicom.__init__(path)
                instance_dicom.export_nifti(file_path=nifti_temp,mode='pet',mask=None)
                # shutil.rmtree(path)