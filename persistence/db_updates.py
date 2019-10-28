import pandas as pd
import psycopg2.extras as ex
import time
from time import gmtime, strftime
from datetime import datetime


def push_to_shoe_request(conn, details):
    date_today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cur = conn.cursor()

    email = details['email']
    shoes = details['shoes']
    size = details['size']
    updates = details['updates']
    gender = details['gender']
    status = 'Pending'

    '''else:
        updates = "Once"'''

    if gender == "Male":
        gender = 'M'
    else:
        gender = 'F'

    sql_query = "INSERT INTO subscriber (subscriber_id , shoe_names , shoe_size ,gender ,frequency, request_date, status ) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    cur.execute(sql_query, (email, shoes, size,
                            gender, updates, date_today, status))

    conn.commit()


def get_customer_data(conn):

    sql = "select * from subscriber where frequency = 'Daily';"

    data = pd.read_sql_query(sql, conn)

    return data


def get_customer_data_instant(conn):

    sql = "select * from subscriber where status = 'Pending';"

    data = pd.read_sql_query(sql, conn)

    return data


def get_price_data(conn):

    sql = "select * from shoe_price_hist;"

    data = pd.read_sql_query(sql, conn)

    return data


def push_price_data(price_df,conn):

    print("inside push price")
    date_today = datetime.now().strftime('%d-%m-%Y')

    cur = conn.cursor()

    for i in range(0, len(price_df)):

        shoename = price_df['name'][i]
        website = price_df['Company'][i]

        print(shoename,website)

        if 's$' in price_df['price'][i].lower() or '$' in price_df['price'][i].lower():
            price = price_df['price'][i].split('$')[1]
            if ',' in price:
                price = price.split(',')[0]

        elif 'sgd' in price_df['price'][i].lower():
            price = price_df['price'][i].split('SGD')[1].split('.')[0]
            
        else:
            price = int(price_df['price'][i])
        
        price = int(price)
        print(price)

        sql_query = "INSERT INTO shoe_price_hist (shoe_name,website,price_date,price) VALUES (%s, %s, %s, %s)"

        cur.execute(sql_query, (shoename, website, date_today, price))

        print("query executed")

        conn.commit()

        print("DB comit")


def push_df_to_subscriberDB(connection, df):
    table = 'subscriber'
    if len(df) > 0:
        df_columns = list(df)
        # create (col1,col2,...)
        columns = ",".join(df_columns)
        # create VALUES('%s', '%s",...) one '%s' per column
        values = "VALUES({})".format(",".join(["%s" for _ in df_columns]))
        # create INSERT INTO table (columns) VALUES('%s',...)
        insert_stmt = "INSERT INTO {} ({}) {}".format(table, columns, values)

        cur = connection.cursor()
        ex.execute_batch(cur, insert_stmt, df.values)
        connection.commit()
        cur.close()


def push_file_to_price_histDB(connection, df):
    table = 'shoe_price_hist'
    if len(df) > 0:
        '''        for i in range(0, len(df)):
                    if 's$' in df[i].lower() or '$' in df[i].lower():
                        price = int(df[i].split('$')[1])
                    else:
                        price = int(df[i])
                    df['price'][i] = price'''
        df_columns = list(df)
        # create (col1,col2,...)
        columns = ",".join(df_columns)
        # create VALUES('%s', '%s",...) one '%s' per column
        values = "VALUES({})".format(",".join(["%s" for _ in df_columns]))
        # create INSERT INTO table (columns) VALUES('%s',...)
        insert_stmt = "INSERT INTO {} ({}) {}".format(table, columns, values)
        cur = connection.cursor()
        ex.execute_batch(cur, insert_stmt, df.values)
        connection.commit()
        cur.close()


def update_status(df,connection):

    # table = 'subscriber'
    # if len(df) > 0:

    #     df['status'] = 'Processed'

    #     df_columns = list(df)
    #     # create (col1,col2,...)
    #     columns = ",".join(df_columns)
    #     # create VALUES('%s', '%s",...) one '%s' per column
    #     values = "VALUES({})".format(",".join(["%s" for _ in df_columns]))
    #     # create INSERT INTO table (columns) VALUES('%s',...)
    #     insert_stmt = "INSERT INTO {} ({}) {}".format(table, columns, values)

    #     cur = connection.cursor()
    #     ex.execute_batch(cur, insert_stmt, df.values)
    #     connection.commit()
    #     cur.close()

    cur = connection.cursor()
    
    for i in range(0,len(df)):

        df['status'][i] = 'Processed'
        
        # sql_query = '''Update subscriber set status = 'Processed' where subscriber_id = '''+ str(df['subscriber_id'][i])+'''
        # and shoe_names = ''' + df['shoe_names'][i]+'''
        # and shoe_size = ''' + df['shoe_size'][i]+'''
        # and gender = ''' + df['gender'][i]+'''
        # and frequency = ''' + df['frequency'][i]+'''
        # and request_date = ''' + df['request_date'][i]+'''
        # and status = 'Pending' '''

        sql_query = "Update subscriber set status = 'Processed' where subscriber_id =\'" + str(df['subscriber_id'][i])+ "\' and shoe_names =\'" + df['shoe_names'][i]+ "\' and shoe_size =  \'"+ df['shoe_size'][i]+ "\' and gender =  \'"+ df['gender'][i]+"\' and frequency =  \'"+ df['frequency'][i]+"\' and request_date =  \'"+ df['request_date'][i]+"\' and status = 'Pending'"

        print(sql_query)

        cur.execute(sql_query)

        print("query executed")

        connection.commit()

        print("DB comit")

