import requests
from zipfile import ZipFile 


def get_dicoms(idSeries):
    file=requests.get('http://localhost:8042/series/'+idSeries+'/archive',auth=('salim','salim'))
    with ZipFile(file, 'r') as zip:      
        zip.extractall('C:/Users/Nicolas/Desktop')