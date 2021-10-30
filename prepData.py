import numpy as np
import utils

def prepData(features, modelNames):
    # too much data for memory so cut down the data by some fraction
    features = utils.getSubset(features, 0.8)

    # Now create the features
    return encode(features, modelNames)

def encode(features, modelNames):
    ''' features: each entry is a variable length list. The entries are enzymes.
    "modelNames" holds a mapping of enzyme -> integer where the integer is an 
    offset into "single_encoding". So if an enzyme "tom" maps to 17, then position
    17 in "single_encoding" is set to 1
    If you look at "single_encoding", each row will add up to an integer equal to the 
    length of the "features" row
    '''
    encoding=[]
    for i in range(len(features)):
        single_encoding=np.zeros(len(modelNames), dtype=np.float16)
        if features[i] != []:
            for single_name in features[i]:
                single_encoding[modelNames.index(single_name)]=1
        encoding.append(single_encoding)
    return encoding