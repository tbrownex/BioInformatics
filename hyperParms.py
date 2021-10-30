import itertools

def getParms():
    L1Size       = [8]
    L2Size       = [8]
    l1Activation = ["tanh"]
    l2Activation = ["relu"]
    batchSize    = [32]
    learningRate = [1e-3]
    std          = [0.25]
    dropout      = [0.3 for n in range(3)]
    optimizer    = ["Adam"]
    return list(itertools.product(L1Size,
                                  L2Size,
                                  l1Activation,
                                  l2Activation,
                                  batchSize,
                                  learningRate,
                                  std,
                                  dropout,
                                  optimizer))