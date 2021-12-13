#Main GUI code for PyAirplay
#This mainly uses Tkinter for simplicity.
class GUI:
    def __init__(self, config):
        self.uiTheme = config["GUI"]["Theme"]
        
        #A lot of work to do here as of 12/10/21 -Ben