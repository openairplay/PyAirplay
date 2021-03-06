version = '0.0.1'

if __name__ == "__main__":
    print("This program is meant to be run from the run script (either ending in .sh, or .bat), errors may occur.")
    choice = input("Continue? (Y/N)")
    if ((choice == "Y") || (choice == "Yes") || (choice == "y") || (choice == "yes")):
        continue
    else:
        quit()

try:
    import logging
except ImportError:
    quit()

logging.basicConfig(filename='latest.log', encoding='utf-8', level=logging.CRITICAL)
logging.info(f'Logging started for PyAirplay - Version {version}')
logging.debug('Importing Libraries')


try:
    #Net Tools
    from zeroconf import Zeroconf as ZC
    from zeroconf import ServiceBrowser as SB
    #Misc Tools
    import configparser as CP
    #UI Tools
    import tkinter as tk
    logging.debug('Libraries imported successfully')
except ImportError:
    logging.critical('Libraries failed to load!')
    logging.critical('Please make sure you have the libraries below or the program will not run!')
    logging.critical('ConfigParser, ZeroConf, Tkinter')
    quit()


#MAKE SURE THESE ARE PROPERLY IMPORTED
#I am bad at setting up local modules -Ben
try:
    #Local Modules
    from ui import GUI as ui
    from net import Network as net
    logging.debug('Local modules imported successfully')
except ImportError:
    logging.critical('Local modules failed to import!')
    logging.critical('Please make sure you are running this file in the folder its supposed to be in. Otherwise reinstall PyAirplay')


#Init
config = CP.ConfigParser()
config.read("config.ini")
if ('General' in config) && ('Network' in config) && ('GUI' in config):
    #Config should have everything in it,
    #leave all the individual entry checking to other parts of the code.
    continue
else:
    formatConfig(config, "ALL")

#Init all external modules.
ap = net()
gui = ui(config)


#Loop
while True:
    #This can be expanded upon later, this is just a general outline.
    #This is to allow the GUI to make calls to other things depending on what function it wants
    #Allowing us to expand the utility of this later on. -Ben
    inputs = gui.doUpdate()
    if inputs[0] == "QUIT":
        ap.end()
        gui.end()
        quit()
    outputs = ap.doUpdate(inputs)
    gui.doneUpdate(outputs)