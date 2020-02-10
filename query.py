import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["bus_routes"]

# Choose a route and a direction
mycol = mydb["2_332990"]

# 3pm
current_time = 15*60

#cl["bus_routes"]["2"]
#mydoc = mycol.find(query)

# Match the time of day
query = { "$match": { 'Minutes' : { "$gte" : current_time-60, "$lt" : current_time+60 } } }
mydoc = mycol.aggregate([ query ])

# Find 

# Return all routes within 1 hour of current time
for x in mydoc:



#def

#             <FramedVehicleJourneyRef>
#                <DataFrameRef>2011-05-25T00:00:00-06:00</DataFrameRef>
#                <DatedVehicleJourneyRef>1179692</DatedVehicleJourneyRef>
#             <VehicleLocation>
#                <Longitude>-111.89173</Longitude>
#                <Latitude>40.7651</Latitude>
#             <PublishedLineName>Route 2 (200 SOUTH)</PublishedLineName>
#          <CourseOfJourneyRef>4730</CourseOfJourneyRef>
#          <VehicleRef>07011</VehicleRef>

"""
events = mdb.events.aggregate([
    {"$match": {"$and" : [{"type": "ClientService"},{"some_key":"value"}]}},
    {"$project": {"value": 1, "day": {"$dayOfYear": "$timestamp"}, "count": {"$add": [1]}}},
    {"$group": {"_id": {"day": "$day", "value": "$value"}, "count": {"$sum": "$count"}}},
    {"$sort": {"day": -1, "value": 1}}
])


db.collection.aggregate([
    {
        '$match': { 
            "user.statuses_count": { "$gte": 100 },
            "user.time_zone": "Brasilia"
        }
    },
    {
        "$group": {
            "_id": "$user.id",
            "max_followers": { "$max": "$user.followers_count" },
            "data": { "$addToSet": "$$ROOT" }
        }
    },
    {
        "$unwind": "$data"
    },   
    {
        "$project": {
            "_id": "$data._id",
            "followers": "$max_followers",
            "screen_name": "$data.user.screen_name",
            "tweets": "$data.user.statuses_count"
        }
    }, 
    {
        "$sort": { "followers": -1 }
    },
    {
        "$limit" : 1
    }
])

"""
