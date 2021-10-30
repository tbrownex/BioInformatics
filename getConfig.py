''' A dictionary object holds key parameters such as:
    - the location and name of the input data file
    - the location and name of the log file
    - the default logging level
    - how many months to use for Test
    - an indicator allowing execution in Test mode'''

__author__ = "Tom Browne"

def getConfig():

    d = {}
    d["dataLoc"]    = '/home/tbrownex/data/bioInformatics/Tutorial/enzyme_prediction/'
    d["logLoc"]     = "/home/tbrownex/"
    d["logFile"]    = "Boeing.log"
    d["logDefault"] = "info"
    d["testPct"]   = 0.20
    return d