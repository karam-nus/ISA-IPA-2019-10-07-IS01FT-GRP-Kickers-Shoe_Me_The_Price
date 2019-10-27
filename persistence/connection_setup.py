import sys, os
import psycopg2
import time
import pandas as pd
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_connection(config, DB_Name = None):
    '''
    Creates connection with Postgres DB server
    :return: Connection object
    '''
    username = config['DATABASE']['USERNAME']
    password = config['DATABASE']['PASSWORD']
    host = config['DATABASE']['HOST']
    port = config['DATABASE']['PORT']
    success = False
    
    while not success:
        try:
            if(DB_Name==None):
                myConnection = psycopg2.connect( host=host, port=port, user=username, password=password)
                print("Connection with DB server successful!")
                success = True
            else:
                myConnection = psycopg2.connect(host=host, port=port, user=username, password=password, dbname=DB_Name)
                print("Connection with DB server successful!")
                success = True
        except:
            print("Error while connecting to DB server... Please check the DB server. \nRetrying Connection in 15 seconds...")
            time.sleep(15)
    return myConnection


def create_tables(connection):
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE subscriber (
    id SERIAL PRIMARY KEY,
    subscriber_id text,
    shoe_names text,
    shoe_size text DEFAULT '8'::text,
    gender text DEFAULT 'M'::text,
    frequency text DEFAULT 'Once'::text,
    request_date text,
    subscription_status text DEFAULT 'Inactive'::text
);
        """, #
        # """ CREATE UNIQUE INDEX subscriber_pkey ON subscriber(id int4_ops);
        #""",
        """
        CREATE TABLE shoe_price_hist (
    id SERIAL PRIMARY KEY,
    shoe_name text,
    website text,
    price_date text,
    price INTEGER
);
        """) #,
        #"""
        #CREATE UNIQUE INDEX shoe_price_hist_pkey ON shoe_price_hist(id int4_ops);
        #""")
    try:
        cur = connection.cursor()
        # create table one by one
        for command in commands:
            # print(command)
            cur.execute(command)
        # close this communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
        
def populate_history(connection):
    history = 'data/price_history.csv' # 'data/price_history.xlsx'
    file = sys.argv[0]
    pathname = os.path.dirname(file)
    history_filepath = os.path.join(pathname,history)
    # print(history_filepath)
    df = pd.read_csv(history_filepath)
    #TODO df.to_sql('shoe_price_hist',connection, if_exists='append')
    
    
def check_Shoe_DB(config,connection):
    '''
    Checks if the shoes DB exists in DB connection, if not, creates the same.
    :return: True if DB exists, else False (creates DB)
    '''
    db_name = config['APP']['DB']
    
    query = f"SELECT datname FROM pg_catalog.pg_database WHERE lower(datname) = lower('{db_name}');"
    databases = pd.read_sql_query(query, connection)
    
    if databases['datname'].count() != 1:
        print("Database doesn't exist, creating the same...")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = connection.cursor()
        create_query = f'CREATE DATABASE {db_name};'
        cur.execute(create_query)
        cur.close()
        connection.close()
        connection = create_connection(config,db_name)
        create_tables(connection)  # Create tables in newly created DB
        populate_history(connection)  # Populate history table with existing data
    else:
        connection.close()
        connection = create_connection(config,db_name)
    return connection

