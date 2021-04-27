def calc():  
    extractor = featureextractor.RadiomicsFeatureExtractor()
    results=extractor.execute(img_pt,mask_3D)
    return results