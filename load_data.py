from pymongo import MongoClient
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import xmltodict
from pathlib import Path
from collections import defaultdict
from dateutil.parser import *

cl = MongoClient()
coll = cl["bus_routes"]
path = Path("./example_data.xml")
master_dict = defaultdict(list)

# DELETE
# x = coll.delete_many({})
# col_list = db.list_collection_names()
cl.drop_database('bus_routes')


#tree = ET.parse("https://www.eventbrite.com/xml/event_search?app_key=USO53E2ZHT6LM4D5RA&country=DE&max=100&date=Future&page=1")
#tree = ET.parse("./example_data.xml")
#root = tree.getroot()

def parse_dir(dir="./data"):
    ## Read many many XML files
    all_trip_snapshots = []
    for p in Path(dir).rglob("*.xml"):
        with p.open( "r") as f:
            d = xmltodict.parse(f.read())
            #time = parse(d["Siri"]["VehicleMonitoringDelivery"]["VehicleActivity"]["RecordedAtTime"])
            if "MonitoredVehicleJourney" in d["Siri"]["VehicleMonitoringDelivery"]["VehicleActivity"]:
                time = parse(d["Siri"]["VehicleMonitoringDelivery"]["VehicleActivity"]["RecordedAtTime"])
                list_of_current_trips = d["Siri"]["VehicleMonitoringDelivery"]["VehicleActivity"]["MonitoredVehicleJourney"]
                for item in list_of_current_trips:
                    item["Time"] = time
                    item["Minutes"] = time.time().minute + time.time().hour * 60
                all_trip_snapshots += list_of_current_trips
    return all_trip_snapshots

all_trip_snapshots = parse_dir()

## Combine them all here, sort observations into route-in-time
for item in all_trip_snapshots:
    item['Longitude'] = item["VehicleLocation"]['Longitude']
    item['Latitude'] = item["VehicleLocation"]['Latitude']
    del item["VehicleLocation"]
    # Combine items based on DatedVehicleJourneyRef 1179692
    master_dict[item["FramedVehicleJourneyRef"]["DatedVehicleJourneyRef"]].append(item)
    # 332991

# Loop through all trips
for key, snapshot_list in master_dict.items():
    # Sort by GPS snap shot date
    sorted(snapshot_list, key = lambda i: i["Time"])
    for i, item in enumerate(snapshot_list):
        if i+1 < len(snapshot_list):
            snapshot_list[i]["TimeElapsed"] = (snapshot_list[i+1]["Time"]-snapshot_list[i]["Time"]).total_seconds()

# We now have a master dict organized by trips
# Add the trip to the appropriate Line/Direction
for key, item in master_dict.items():
    line_and_direction = item[0]["LineRef"]+"_"+item[0]["DirectionRef"]
    cl["bus_routes"][line_and_direction].insert(item)


# Define a document to be an entire trip; OR have each snapshot be a document
