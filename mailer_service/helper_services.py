import pandas as pd

def dataframe_for_subscriber(details_list):

     subscriber_columns = ['subscriber_id', 'shoe_names','request_date']
     df = pd.DataFrame(details_list,columns=subscriber_columns)
     return df