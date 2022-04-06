from app.services.tle_resource import TLEResource
from config.config import CONFIG_APP
from pathlib import Path
from orbit_predictor.locations import ARG
from app.locations.list import LOCATIONS_GET
    
def test_load_from_file_dataset():
    sample = TLEResource()    
    sample.set_dataset(sample.load_resource_file())
    sample.generate_dataset()
    listTLE = sample.get_TLE()
    assert len(listTLE) == 5409
    
def test_one_tle_lines():
    text = "CZ-4B R/B\n"
    text = text + "1 25732U 99025C   22095.55316981  .00000042  00000+0  42311-4 0  9990\n"
    text = text + "2 25732  98.8639 137.0920 0038163 134.8555 351.6391 14.17718628184925\n"
    sample = TLEResource()
    TLE = sample.convertTLE(text)
    assert TLE.name == "CZ-4B R/B"
    
def test_multi_tle():
    text = "CZ-4B R/B\n"
    text = text + "1 25732U 99025C   22095.55316981  .00000042  00000+0  42311-4 0  9990\n"
    text = text + "2 25732  98.8639 137.0920 0038163 134.8555 351.6391 14.17718628184925\n"
    text = text + "OKEAN-O\n"
    text = text + "1 25860U 99039A   22095.55679955  .00000632  00000+0  97507-4 0  9992\n"
    text = text + "2 25860  98.1484 134.7603 0000836  86.7802 273.3503 14.76872672222491\n"
    text = text + "SL-16 R/B\n"
    text = text + "1 25861U 99039B   22095.53550834  .00000550  00000+0  82291-4 0  9998\n"
    text = text + "2 25861  98.1866 121.3027 0015113 202.7387 157.3156 14.78758729224721\n"
    sample = TLEResource()
    sample.set_dataset(text)
    sample.generate_dataset()
    listTLE = sample.get_TLE()
    assert len(listTLE) == 3
    assert listTLE[0].name == "CZ-4B R/B"
    assert listTLE[1].name == "OKEAN-O"
    assert listTLE[2].name == "SL-16 R/B"
    
def test_sats():
    text = "CZ-4B R/B\n"
    text = text + "1 25732U 99025C   22095.55316981  .00000042  00000+0  42311-4 0  9990\n"
    text = text + "2 25732  98.8639 137.0920 0038163 134.8555 351.6391 14.17718628184925\n"
    text = text + "OKEAN-O\n"
    text = text + "1 25860U 99039A   22095.55679955  .00000632  00000+0  97507-4 0  9992\n"
    text = text + "2 25860  98.1484 134.7603 0000836  86.7802 273.3503 14.76872672222491\n"
    text = text + "SL-16 R/B\n"
    text = text + "1 25861U 99039B   22095.53550834  .00000550  00000+0  82291-4 0  9998\n"
    text = text + "2 25861  98.1866 121.3027 0015113 202.7387 157.3156 14.78758729224721\n"
    sample = TLEResource()
    sample.set_dataset(text)
    sample.generate_dataset()
    sats = sample.get_satellites()
    names=[]
    names.append("CZ-4B R/B")
    names.append("OKEAN-O")
    names.append("SL-16 R/B")
    count = 0
    for sate_name, tle in sats.items():
        assert sate_name == names[count]
        count = count + 1
        
def test_predictor():
    
    text = "CZ-4B R/B\n"
    text = text + "1 25732U 99025C   22095.55316981  .00000042  00000+0  42311-4 0  9990\n"
    text = text + "2 25732  98.8639 137.0920 0038163 134.8555 351.6391 14.17718628184925\n"
    text = text + "OKEAN-O\n"
    text = text + "1 25860U 99039A   22095.55679955  .00000632  00000+0  97507-4 0  9992\n"
    text = text + "2 25860  98.1484 134.7603 0000836  86.7802 273.3503 14.76872672222491\n"
    text = text + "SL-16 R/B\n"
    text = text + "1 25861U 99039B   22095.53550834  .00000550  00000+0  82291-4 0  9998\n"
    text = text + "2 25861  98.1866 121.3027 0015113 202.7387 157.3156 14.78758729224721\n"
    sample = TLEResource()
    sample.set_dataset(text)
    sample.generate_dataset()
    predictor = sample.get_predictor_tle("OKEAN-O")
    assert predictor is not None
    
def test_predictor_using():
    
    text = "CZ-4B R/B\n"
    text = text + "1 25732U 99025C   22095.55316981  .00000042  00000+0  42311-4 0  9990\n"
    text = text + "2 25732  98.8639 137.0920 0038163 134.8555 351.6391 14.17718628184925\n"
    text = text + "OKEAN-O\n"
    text = text + "1 25860U 99039A   22095.55679955  .00000632  00000+0  97507-4 0  9992\n"
    text = text + "2 25860  98.1484 134.7603 0000836  86.7802 273.3503 14.76872672222491\n"
    text = text + "SL-16 R/B\n"
    text = text + "1 25861U 99039B   22095.53550834  .00000550  00000+0  82291-4 0  9998\n"
    text = text + "2 25861  98.1866 121.3027 0015113 202.7387 157.3156 14.78758729224721\n"
    sample = TLEResource()
    sample.set_dataset(text)
    sample.generate_dataset()
    predictor = sample.get_predictor_tle("OKEAN-O")
    pass_orbit = predictor.get_next_pass(ARG)
    assert pass_orbit is not None
    
def test_predictor_using_param():
    
    text = "CZ-4B R/B\n"
    text = text + "1 25732U 99025C   22095.55316981  .00000042  00000+0  42311-4 0  9990\n"
    text = text + "2 25732  98.8639 137.0920 0038163 134.8555 351.6391 14.17718628184925\n"
    text = text + "OKEAN-O\n"
    text = text + "1 25860U 99039A   22095.55679955  .00000632  00000+0  97507-4 0  9992\n"
    text = text + "2 25860  98.1484 134.7603 0000836  86.7802 273.3503 14.76872672222491\n"
    text = text + "SL-16 R/B\n"
    text = text + "1 25861U 99039B   22095.53550834  .00000550  00000+0  82291-4 0  9998\n"
    text = text + "2 25861  98.1866 121.3027 0015113 202.7387 157.3156 14.78758729224721\n"
    sample = TLEResource()
    sample.set_dataset(text)
    sample.generate_dataset()
    predictor = sample.get_predictor_tle("OKEAN-O")
    pass_orbit = predictor.get_next_pass(LOCATIONS_GET.get("CHILE"))
    assert pass_orbit is not None
    
    
    