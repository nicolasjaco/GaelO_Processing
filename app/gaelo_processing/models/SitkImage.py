import SimpleITK
import numpy as np


def get_metadata_dictionary(image: SimpleITK.Image) -> dict:
    dictionary = dict()
    for key in image.GetMetaDataKeys():
        value = image.GetMetaData(key)
        dictionary[key] = np.array(value)
    return dictionary
