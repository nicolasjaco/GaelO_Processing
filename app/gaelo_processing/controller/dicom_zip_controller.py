import tempfile

from django.http import HttpResponse

def handle(request):
    method = request.method 
    if(method=='POST'):
        zip_file=request.read()
        filename=get_dicom_zip(zip_file)
        return HttpResponse(status=200)

def get_dicom_zip(zip_file):
    destination=tempfile.mkdtemp(prefix='dicom_zip_')
    file = open(destination+'/dicom.zip', 'wb')
    file.write(zip_file)
    file.close()
    #TODO : UNZIP and CREATE NIFTI
    return file.name