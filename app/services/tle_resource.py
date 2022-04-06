from asyncio.log import logger
import logging
from shutil import ExecError
from tletools import TLE
from config.config import CONFIG_APP
import requests
from orbit_predictor.sources import get_predictor_from_tle_lines

class TLEResource(object):
    
    def __init__(self):
        self.datos=''
        self.satellites = {}
        self.listle = []
        
    def get_resource(self):
        try:
            url = CONFIG_APP["app"]["provider_active_satellites"]
            filepath=CONFIG_APP["app"]["file_resource"]
            resource = requests.get(url)
            
            if (resource.status_code==200):
                file1 = open(filepath, 'w')
                file1.writelines(resource.text)
                file1.close()
            else:
                raise Exception("GET resource FAIL")
            
        except Exception as e:
            logging.debug("Exception on get_resource: {}".format(e))
            
    def load_resource_file(self):
        try:
            filepath=CONFIG_APP["app"]["file_resource"]
            file1 = open(filepath, 'r')
            lines = file1.readlines()
            ##TODO fixit performance
            str= ""
            for item in lines:
                str = str + item.strip() + "\n"
            last = len(str)
            str = str[:last-1]
            return str
        except Exception as e:
            logging.debug("Exception on get_resource: {}".format(e))
            raise Exception(e)
    
    def set_dataset(self,tlelist):
        self.datos = tlelist
        
    def get_lines(self):
        return self.datos
    
    def convertTLE(self,lines):
        tle_lines = lines.strip().splitlines()
        self.satellites.setdefault(tle_lines[0],(tle_lines[1],tle_lines[2]))
        return TLE.from_lines(*tle_lines)
    
    def convert_lines_to_tle(self,lines):
        try:
            countTLE = 0
            strTLE=""
            
            if ((len(lines) % 3)==1):
                raise Exception("LIST not compatible")
            
            for item in lines:
                if (countTLE<3):
                    strTLE = strTLE + item + "\n"
                    countTLE=countTLE + 1
                else:
                    self.listle.append(self.convertTLE(strTLE))
                    countTLE = 1
                    strTLE = ""
                    strTLE = strTLE + item + "\n"
            
            if (countTLE==3):
                self.listle.append(self.convertTLE(strTLE))
                
        except Exception as e:
            logging.debug("Exception on convertLinesToTLE: {}".format(e))
            raise Exception(e)

    def generate_dataset(self):
        try:
            self.convert_lines_to_tle(self.get_lines().strip().splitlines())
        except Exception as e:
            logging.debug("Exception on convertLinesToTLE: {}".format(e))
            raise Exception(e)
            
        
    def get_TLE(self):
        return self.listle
    
    def get_satellites(self):
        return self.satellites
    
    def get_predictor_tle(self,name):
        sats = self.get_satellites()
        try:
            predictor = None
            ##TODO Fix performance
            if sats.get(name):
                tupla = sats.get(name)
                predictor = get_predictor_from_tle_lines(tupla)
                
            return predictor
        except Exception as e:
            logging.debug("Exception on get_predictor: {}".format(e))
            raise Exception(e)
        
            
        
            
        
        
        
        