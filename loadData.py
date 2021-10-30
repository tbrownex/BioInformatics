from loadPickle import loadPickle

def loadData(config, fileName):
    # Get the model names in a list
    # A few random entries I checked are either proteins or genes
    return loadPickle(config['dataLoc']+fileName)