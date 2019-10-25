'''
1. Create gmail connection
2. Check for unread mails
3. Fetch unread mails
4. Mark them read in gmail
5. Filter relevant mails
6. Push to DB in predefined format
7. Run robos
8. Save the output in history table
9. Mail replies

'''
from mailer_service import gmail_services,helper_services
import persistence as p
from robots import bot_controller

import pandas as pd

def execute_gmail_fetch(connection):
     # Make Connection
     service = gmail_services.connect_gmail()    # returns service object
     # Get Messages
     relevant_messages = gmail_services.get_relevant_emails(service)      # List of filtered unread messages
     # Extract emaidID, Subject
     relevant_details_list = gmail_services.get_info_from_mail(relevant_messages)    # List of dictionaries
     
     #CALL BOTS

     df = bot_controller.execute_bots_for_mail(relevant_details_list)

     

     if len(relevant_details_list)!=0:
          df = pd.DataFrame(relevant_details_list)# df = helper_services.dataframe_for_subscriber(relevant_details_list)
          p.db_updates.push_df_to_subscriberDB(connection,df)