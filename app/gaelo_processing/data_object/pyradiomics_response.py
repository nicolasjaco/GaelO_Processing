import numpy as np

from json import JSONEncoder
from collections import OrderedDict


class pyradiomics_response:
    def __init__(self, results :OrderedDict):
        self.results=results

    def get_dictionary(self) -> dict :
        dictionary=dict()
        for key, value in self.results.items():
            if isinstance(value,np.ndarray) or isinstance(value, np.float64):
                dictionary[key] = np.array(value)       
            else:
                dictionary[key] =value
        # print(dictionary)
        return dictionary

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):       
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

  