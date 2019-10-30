import sys, os
import configparser
import persistence as p
import run_processes as rp

# 0. check for the correct path and then import configurations
def config_connect():
	config_file = 'configurations.ini'
	file = sys.argv[0]
	pathname = os.path.dirname(file)
	print('[System]Running from %s' % os.path.abspath(pathname))
	#print('file is %s' % file)
	if len(pathname)==0: pathname='.'
	if ('credentials.json' in os.listdir(pathname)):print("[System]Credentials found")
	else:print("[System]Credentials NOT found")
	if config_file in os.listdir(pathname):
	     config = configparser.ConfigParser()
	     config.read(os.path.join(pathname,config_file))
	     # print({section: dict(config[section]) for section in config.sections()})
	     
	# 1. make connection
	     First_db_connection = p.connection_setup.create_connection(config)

	# 2. check if the DB exists - if not - create. return - new DB connection
	     db_connection = p.connection_setup.check_Shoe_DB(config, First_db_connection)
	return db_connection