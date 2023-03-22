import os
from pathlib import Path
import configparser

class ReadConfiguration():
    def __init__(self):
        path = Path(__file__)
        ROOT_DIR = path.parent.parent.absolute()
        config_path = os.path.join(ROOT_DIR, "config.txt")
        self.config = configparser.ConfigParser()
        self.config.read(config_path)   
    
    def getValueFromConfig(self,key):
        return self.config.get('global',key)