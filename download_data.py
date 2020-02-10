import time
import requests
import argparse
import lxml.etree as etree
from io import StringIO
from utils import *
item = ""

s = requests.Session()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
s.headers.update({'user-agent': user_agent})

bus_stop_url = "http://api.rideuta.com/SIRI/SIRI.svc/StopMonitor?stopid=821006&minutesout=120&onwardcalls=true&filterroute=822&usertoken=UUBIRBIBF1A"
route_url = "http://api.rideuta.com/SIRI/SIRI.svc/VehicleMonitor/ByRoute?route=822&onwardcalls=true&usertoken=UUBIRBIBF1A"
url = route_url

## Main loop
while True:
    page = s.get(url, verify=False).content #.decode()
    xml = etree.fromstring(page)
    xml_out = etree.tostring(xml, pretty_print=True)
    fpath = increment_path("download.xml", make_directory=False, base_path="data")
    with open(fpath, "wb") as f:
        f.write(xml_out)
    print("Done with {}".format(fpath))
    time.sleep(30)

