# This is just to see what's in these files
import random

def getRandom(x):
    print(random.choices(x, k=5))

def getSubset(data, frac):
    assert (frac < 1.0 and frac > 0), "invalid fraction to sample"
    k = int(len(data)*frac)
    return random.choices(data, k=k)

# Confirm all entries are present in modelNames
def confirmNames(file, modelNames):
    found = nf = 0
    for enzyme in file:
        for e in enzyme:
            if e in modelNames:
                found+=1
            else:
                nf+=1
    print("found: ", found)
    print("not found: ", nf)