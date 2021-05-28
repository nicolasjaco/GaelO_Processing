from django.test import TestCase

from ...gaelo_processing.utips.utips import Utips

class MyTest(TestCase):
    def test_extract_zip_files(self):
        file_zip=Utips.unzip_file("C:/Users/Nicolas/AppData/Local/Temp/orthanc_zip_p5gg0sut/orthanc.zip")
        print('test extract_zip_files validate')