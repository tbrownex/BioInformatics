import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"

import numpy as np
import tensorflow as tf
from pathlib import Path
import time
import gc

from getConfig import getConfig
from splitData import splitData
from buildModel import buildModel
from loadData import loadData
from prepData import prepData
from hyperParms import getParms
import utils
from getArgs import getArgs

# This file stores the results for each set of parameters so you can review a series
# of runs later
def writeResults(results):
    delim = ","
    home = str(Path.home())
    with open(home+"/NNscores.csv", 'w') as summary:
        hdr = "L1"+delim+"L2"+delim+"L1activation"+delim+"L2activation"+\
            delim+"batchSize"+delim+"LR"+delim+"StdDev"+delim+"Dropout"+\
        delim+"optimizer"+delim+"Loss"+delim+"Accuracy"+"\n"
        summary.write(hdr)
        
        for x in results:
            rec = str(x[0][0])+delim+str(x[0][1])+delim+str(x[0][2])+\
            delim+str(x[0][3])+delim+str(x[0][4])+delim+str(x[0][5])+\
            delim+str(x[0][6])+delim+str(x[0][7])+delim+str(x[0][8])+\
            delim+str(x[1])+delim+str(x[2])+"\n"
            summary.write(rec)

def setLabels(enzymeLength, non_enzymeLength):
    # Add the label. 1 means "enzyme"; 0 means "not an enzyme"
    labels = np.concatenate([np.ones([enzymeLength, 1]),
                             np.zeros([non_enzymeLength, 1])],
                            axis=0).flatten()
    return tf.keras.utils.to_categorical(labels, num_classes=2)

def loadParms(x):
    ''' Load a dictionary with the hyperparameter combinations for one run '''
    d = {}
    d['l1Size']      = x[0]
    d['l2Size']      = x[1]
    d['l1Activation']= x[2]
    d['l2Activation']= x[3]
    d['batchSize']   = x[4]
    d['lr']          = x[5]
    d['std']         = x[6]
    d['dropout']     = x[7]
    d['optimizer']   = x[8]
    return d

if __name__ == "__main__":
    args   = getArgs()
    config = getConfig()
    
    modelNames = loadData(config, 'Pfam_model_names_list.pickle')
    enzyme_features = loadData(config, 'Pfam_name_list_new_data.pickle')
    non_enzyme_features = loadData(config, 'Pfam_name_list_non_enzyme.pickle')
    
    enzyme_features = prepData(enzyme_features, modelNames)
    non_enzyme_features = prepData(non_enzyme_features, modelNames)
    
    # This will be the input data with zeros and ones in various columns
    # Each column corresponds to an enzyme or protein
    features = np.concatenate([enzyme_features, non_enzyme_features], axis=0)
    
    labels = setLabels(len(enzyme_features), len(non_enzyme_features))
    assert (len(labels) == len(features)), "length mismatch between features and labels"
    
    x_train, x_test, y_train, y_test = splitData(features, labels, config)
    parms = getParms()
    epochs = args.epochs
    numFeatures = features.shape[1]
    
    results = []
    count = 1
    
    start_time = time.time()
    print("\n{} parameter combinations".format(len(parms)))
    #print("\n{:<10}{}".format("Test loss","Test accuracy"))
    count=0
    for x in parms:
        print(count)
        count+=1
        parmDict = loadParms(x)
        model = buildModel(numFeatures, parmDict)
        model.compile(loss='categorical_crossentropy',
                      optimizer=tf.keras.optimizers.Adam(),
                      metrics=['accuracy'])
        history = model.fit(x_train, y_train,
                            batch_size=parmDict['batchSize'],
                            epochs=epochs,
                            verbose=0,
                            validation_data=(x_test, y_test))
        score = model.evaluate(x_test, y_test, verbose=0)
        gc.collect()
        tf.keras.backend.clear_session()
        tup = (x, round(score[0], 3), round(score[1], 3))
        results.append(tup)
    # Write out a summary of the results
    writeResults(results)
    print("\ncomplete after {:,.0f} minutes".format((time.time()-start_time)/60))
    #model.summary()
    #for layer in model.layers:
    #    print(layer.get_output_at(0).get_shape().as_list())