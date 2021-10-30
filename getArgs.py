''' Get the command line arguments:
    Mandatory
    - epochs
    
    Optional arguments
    - None  '''

import argparse

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", \
                        type=int)
    return parser.parse_args()