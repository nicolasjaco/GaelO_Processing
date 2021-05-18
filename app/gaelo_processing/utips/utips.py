from zipfile import ZipFile 
import tempfile
import os
import shutil

class Utips:
    def unzip_file(self, zip_file :str): #,destination:str  ):#passer en static   
        destination=tempfile.mkdtemp(prefix='dezip_', dir='C:/Users/Nicolas/Desktop')     
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
        # shutil.rmtree(destination)
        

    
    