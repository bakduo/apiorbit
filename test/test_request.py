
from config.config import CONFIG_APP
import requests

def test_request():
    
    url = CONFIG_APP["app"]["provider_active_satellites"]

    resource = requests.get(url)

    assert resource.status_code==200
    