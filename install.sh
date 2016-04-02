# Run script
# rethinkdb

sudo apt-get install python-pip
source /etc/lsb-release && echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list wget -qO- http://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -

sudo apt-get update
sudo apt-get install nodejs


sudo apt-get install  -y --force-yes nodejs npm rethinkdb build-essential

sudo cp instance1.conf /etc/rethinkdb/instances.d/instance1.conf


#sudo iptables -A INPUT -p tcp --destination-port 29015 -j DROP

sudo iptables -A INPUT -p tcp --destination-port 8080 -j DROP

sudo iptables -I INPUT -s 127.0.0.1 -p tcp --dport 8080 -j ACCEPT

sudo npm install -g strongloop
