import hashlib

from django.conf import settings

from dicom_to_cnn.tools.pre_processing import series


class DicomToCnn:
    def to_nifti(self,folder_path: str):
        """[Get DICOM seerie path and transform to nifti]

        Args:
            folder_path (str): [DICOM series folder path]
        """
        data_path = settings.STORAGE_DIR
        path = folder_path       
        nifti=series.get_series_object(path)        
        nifti_str=str(nifti)
        nifti_str=nifti_str[1:44]
        if nifti_str=='dicom_to_cnn.model.reader.SeriesCT.SeriesCT':  
            nifti.get_instances_ordered()   
            nifti.get_numpy_array()
            image_md5 = hashlib.md5(str(nifti).encode())
            image_id = image_md5.hexdigest()
            img=nifti.export_nifti(data_path+'/image/image_'+image_id+'.nii')
        if nifti_str=='dicom_to_cnn.model.reader.SeriesPT.SeriesPT':
            nifti.get_instances_ordered()   
            nifti.get_numpy_array()
            nifti.set_ExportType('suv')
            image_md5 = hashlib.md5(str(nifti).encode())
            image_id = image_md5.hexdigest()
            img=nifti.export_nifti(data_path+'/image/image_'+image_id+'.nii')