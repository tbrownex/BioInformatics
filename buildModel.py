import tensorflow as tf
import tensorflow.keras.layers as KL

def buildModel(numFeatures, parmDict):
    l1 = parmDict['l1Size']
    l2 = parmDict['l2Size']
    dropout = parmDict['dropout']
    l1act = parmDict['l1Activation']
    l2act = parmDict['l2Activation']
    model = tf.keras.models.Sequential()
    model.add(KL.Dense(l1, activation=l1act, input_shape=(numFeatures,)))
    model.add(KL.Dropout(dropout))
    model.add(KL.Dense(l2, activation=l2act))
    model.add(KL.Dropout(dropout))
    model.add(KL.Dense(units=2, activation='softmax'))
    return model