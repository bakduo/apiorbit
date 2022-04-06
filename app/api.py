from email import message
from app import app
from config.config import CONFIG_APP
from flask import request, jsonify
import json
import logging
from app.locations.list import LOCATION_ENABLED,LOCATIONS_GET
from app.services.tle_resource import TLEResource

resource_tle = TLEResource()
resource_tle.set_dataset(resource_tle.load_resource_file())
resource_tle.generate_dataset()

def valid_location_name(name):
    if ((name.lower() in LOCATION_ENABLED) or (name.upper() in LOCATION_ENABLED)):
        return True
    return False

def canonical_name(name):
    
    if (name.lower() in LOCATION_ENABLED):    
        return name.lower()
    
    if (name.upper() in LOCATION_ENABLED):
        return name.upper()
    
    return False
    
#TODO FIXIT real healthy
@app.route('/health',methods=['GET'])
def status():
    sample = {}
    sample['status']=True
    return json.dumps(sample), 200

#TODO FIXIT security layer
@app.route('/api/v1/reload',methods=['POST'])
def set_resources():
    try:
        json_data = request.get_json()
        token = json_data["cmdb3937aafaa8971c0"]
        if (token==CONFIG_APP["app"]["cmdb3937aafaa8971c0"]):
            resource_tle.get_resource()
            return jsonify(message="Resources updated"), 200
        
        return jsonify(message="Don't permit modified resources"), 200
    except Exception as e:
        logging.debug("get_satellites :{}".format(e))
        return jsonify(message="{}".format(e)), 500


@app.route('/api/v1/sats',methods=['GET'])
def get_satellites():
    try:
        satslist = resource_tle.get_satellites().keys()
        ##For serialize keys
        return jsonify(sats=list(satslist)), 200
    except Exception as e:
        logging.debug("get_satellites :{}".format(e))
        return jsonify(message="{}".format(e)), 500


@app.route('/api/v1/orbit',methods=['POST'])
def pcountry():
    try:
        json_data = request.get_json()
        country = json_data["country"]
        sat = json_data["sat"]
        
        if (valid_location_name(country)):
            logging.debug("Check location :{}".format(country))
            predictor = resource_tle.get_predictor_tle(sat)
            logging.debug("Check predictor :{}".format(predictor))
            if (predictor is not None):
                canonical = canonical_name(country)
                if (canonical):
                    predicted_pass = predictor.get_next_pass(LOCATIONS_GET.get(canonical))
                    if (predicted_pass is not None):
                        try:
                            result_predictor = "Result: {}".format(predicted_pass)
                            position = predictor.get_position(predicted_pass.aos)
                            logging.debug("Check position :{}".format(position))
                            if (LOCATIONS_GET.get(canonical).is_visible(position)):
                                return jsonify(message="It's visisble on {}  {}".format(canonical,result_predictor)),200
                            else:
                                return jsonify(message="It's not visisble on {}".format(canonical)),200
                        except Exception as e:
                            logging.debug("Exception convert str result :{}".format(e))
                
        return jsonify(message="Don't available zone"), 404
    except Exception as e:
        logging.debug("/api/v1/orbit :{}".format(e))
        return jsonify(message="{}".format(e)), 500
        
        
    