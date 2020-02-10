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