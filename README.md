# Install:

	wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
	echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
	sudo apt-get update
	sudo apt-get install -y mongodb-org

# Start
	sudo service mongod start
	sudo service mongod status
    http://localhost:27017/
    
# Web API
    mongod --rest --httpinterface
    http://localhost:28017/

# UTA Project
For this project, we harvest UTA bus transit data to predict bus arrival times based on the last reported GPS location of a bus. One could also use this database to evaluate the distribution of actual arrival times against scheduled ones, which may be of particular interest to help one know when is “too early” to arrive at the bus stop, or when should they really arrive when there is inclement weather.

## Data
The data was acquired through the UTA API, which is periodically queried to obtain bus location data. The data was then processed to record a document that contained the route number, the time of day, all queried locations, and the time it takes to reach the next location.

## Algorithms
The idea here is that a user can give the system a route, time of day, current bus location, and bus destination, and the system would query the Mongo database for all documents matching the route and time of day. For each returned document, the nearest recorded location to the bus’s position and destination is found, and, if the recorded locations are sufficiently close to the queried ones (which can also be done in the query step), we sum over all of the intermediary locations to find an estimated elapsed time to traverse between the current location and destination (this assumes buses don’t have particularly circuitous routes, which is true for me, at least). These are then averaged together to find a better estimate of the bus’s ETA.

Note that this database could easily be extended to include traffic or weather with each document, allowing queries to be further filtered to better match the conditions in the user’s query.

Another next step for this database would be to attach bus stop IDs to the geographic locations nearest to them. This would help simplify the previous process for user’s querying bus stop IDs as the destination, and would make it possible for one to evaluate historical arrival patterns at a particular bus stop more easily.
