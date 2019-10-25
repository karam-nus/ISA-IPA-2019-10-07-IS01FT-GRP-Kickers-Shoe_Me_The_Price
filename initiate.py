'''
Usage - python3 initiate.py
0. check for the correct path and then import configurations
1. make connection
2. check if the DB exists - if not - create
3. check if the tables exist - if not - create
4. Populate predefined table data
5. proceed to start threads

'''
import sys, os
import configparser
import persistence as p
import run_processes as rp

# 0. check for the correct path and then import configurations
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
#    TODO add exception handling for created = False in this func

# 3. check if the tables exist - if not - create
# 4. Populate predefined table data
# Handled in DB creation function above
     print("Env Ready!")

# 5. proceed to start threads
     rp.execute_processes(db_connection)

