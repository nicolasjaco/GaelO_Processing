from radiomics import featureextractor
import SimpleITK as sitk
from ..data_object.pyradiomics_response import pyradiomics_response
import json
# import jsonschema
# import schema
from ..exceptions.gaelo_processor_exeptions import GaelOBadRequestException, GaelONotFoundException

class pyradiomics_adapter:
    
    def calculate(self, image : sitk.Image, mask : sitk.Image, json_parms :str ) -> pyradiomics_response :
        """[Trigger pyRadiomics calculation]

        Args:
            image (sitk.Image): [Input Image]
            mask (sitk.Image): [Input mask]

        Returns:
            pyradiomics_response: [Handler for pyRadiomics reponse]
        """              
        extractor = featureextractor.RadiomicsFeatureExtractor()
        extractor.loadJSONParams(json_parms)
        results=extractor.execute(image,mask)
        return pyradiomics_response(results)   
      

          
