import tempfile
import os
import shutil
from zipfile import ZipFile 

class Utips:    
    def unzip_file(zip_file :str): #,destination:str  ): 
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
        # return destination
        # os.remove(zip_file)