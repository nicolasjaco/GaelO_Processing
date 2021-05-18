import requests

# import tempfile

class Orthanc:

    def get_zip_from_orthanc(self, orthanc_series_id):
        file=requests.get('http://localhost:8042/series/'+orthanc_series_id+'/archive',auth=('salim','salim'))
        content=file.content
        zip_file = open('orthanc.zip', 'wb')
        zip_file.write(content)
        zip_file.close()
        return zip_file.name