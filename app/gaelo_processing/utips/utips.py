import tempfile
import os
import shutil

from zipfile import ZipFile

from PIL.Image import NONE 

class Utips:    
    def unzip_file(zip_file :str) -> NONE:  
        """[Extract the zip files]

        Args:
            zip_file (str): [The zip link]

        Returns:
            NONE
        """
        destination=tempfile.mkdtemp(prefix='gaelo_pross_unzip_') 
        with ZipFile(zip_file) as my_zip:
            for member in my_zip.namelist():
                filename = os.path.basename(member)
                # skip directories
                if not filename:
                    continue        
                # copy file (taken from zipfile's extract)                
                source = my_zip.open(member)
                target = open(os.path.join(destination, filename), "wb")
                with source, target:                   
                    shutil.copyfileobj(source, target)
        # os.remove(zip_file)