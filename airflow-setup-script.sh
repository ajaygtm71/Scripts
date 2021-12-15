#!/bin/bash
# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
# (optional)
#Install MySQL -Client
#Define user name of linux user where the software will be installed

username=sancususer
type=mysql
db_hostname=10.10.105.18
db_schemaname=sancus_dev #If we want to run it for DEV change accordingly
db_username=sancusadmin@sancus-core-db
db_password=Tredence@123
port=3306
#pluginURL=https://github.com/teamclairvoyant/airflow-rest-api-plugin.git
pluginURL=https://github.com/teamclairvoyant/airflow-rest-api-plugin/archive/
version=v1.0.5-branch.zip

sudo apt-get update
sudo apt install -y python3-pip
sudo apt-get install -y jq

sudo apt-get install -y python-dev libmysqlclient-dev
sudo pip3 install mysqlclient
sudo apt-get -y install sshpass
sudo apt install -y mysql-client-core-5.7

sudo pip3 install azure-mgmt-hdinsight
sudo pip3 install azure
sudo pip3 install mysql-connector-python
sudo pip3 install pymysql

mkdir /home/$username/airflow
export AIRFLOW_HOME=/home/$username/airflow

# install from pypi using pip
sudo pip3 install apache-airflow==1.10.3
sudo pip3 install --upgrade Flask
sleep 30s
airflow version
#Download rest plugin
#git clone $pluginURL /home/$username/restplugin/
#git checkout -b v1.0.5-branch
#cp -r /home/$username/restplugin/plugins /home/$username/airflow/

#Download rest plugin
curl -L $pluginURL$version -o /home/$username/restplugin
sudo apt install unzip
unzip /home/$username/restplugin
cp -R /home/$username/airflow-rest-api-plugin-1.0.5-branch/plugins /home/$username/airflow/
rm -rf /home/$username/restplugin /home/$username/airflow-rest-api-plugin-1.0.5-branch
sudo pip3 uninstall Werkzeug
sudo pip3 install Werkzeug==0.15.6
#Below line adds authentication for REST Plugin
echo """

[environment_variables]
#Environment variable for this environment
env = dev

[rest_api_plugin]

# Logs global variables used in the REST API plugin when the plugin is loaded. Set to False by default to avoid too many logging messages.
# DEFAULT: False
log_loading = False

# Filters out loading messages from the standard out
# DEFAULT: True
filter_loading_messages_in_cli_response = True

# HTTP Header Name to be used for authenticating REST calls for the REST API Plugin
# DEFAULT: 'rest_api_plugin_http_token'
rest_api_plugin_http_token_header_name = aidcUI

# HTTP Token  to be used for authenticating REST calls for the REST API Plugin
# DEFAULT: None
# Comment this out to disable Authentication
rest_api_plugin_expected_http_token = 1af538baa9045a84c0e12321213483ff24

""" >> /home/$username/airflow/airflow.cfg


DB_END_PT="sql_alchemy_conn = "$type"://"$db_username":"$db_password"@"$db_hostname":"$port"/"$db_schemaname

#Configure the database
Var1='sql_alchemy_conn = .*'
#Var2='sql_alchemy_conn = mysql://aidccore@aidc-core:Tredence@123@aidc-core.mysql.database.azure.com:3306/aidc_dev'
sed -i "s|$Var1|$DB_END_PT|g" /home/$username/airflow/airflow.cfg

mkdir /home/$username/airflow-bootstrap-scripts
touch /home/$username/airflow-bootstrap-scripts/airflow_web.sh
touch /home/$username/airflow-bootstrap-scripts/log.txt
chmod 777 -R /home/$username/airflow-bootstrap-scripts
mkdir /home/$username/airflow/dags/
chmod 777 -R /home/$username/airflow/dags
mkdir /home/$username/airflow/logs/yarn_logs
mkdir /home/$username/airflow/logs/yarn_logs/preprocess/
mkdir /home/$username/airflow/logs/yarn_logs/packagecheck
mkdir /home/$username/airflow/logs/yarn_logs/loadtodb
mkdir /home/$username/airflow/logs/yarn_logs/dedup
chmod 777 -R /home/$username/airflow/logs/yarn_logs


echo """
#export PATH=/usr/local/bin
sudo rm -rf /home/sancususer/airflow/airflow-*

sudo -E /usr/local/bin/airflow webserver -p 8081 -D
a=\$?
echo \$a >> /home/sancususer/airflow-bootstrap-scripts/log.txt
echo \`date\`>>/home/sancususer/airflow-bootstrap-scripts/log.txt

echo "Welcome to Airflow Webserver ">>/home/sancususer/airflow-bootstrap-scripts/log.txt

sudo -E /usr/local/bin/airflow scheduler -D
b=\$?
echo \$b >> /home/user/airflow-bootstrap-scripts/log.txt
echo \`date\`>>/home/sancususer/airflow-bootstrap-scripts/log.txt

echo "Welcome to Airflow Scheduler">>/home/sancususer/airflow-bootstrap-scripts/log.txt

""" >> /home/$username/airflow-bootstrap-scripts/airflow_web.sh

cat <(crontab -l) <(echo "@reboot /home/sancususer/airflow-bootstrap-scripts/airflow_web.sh") | crontab -

# initialize the database
# airflow initdb

