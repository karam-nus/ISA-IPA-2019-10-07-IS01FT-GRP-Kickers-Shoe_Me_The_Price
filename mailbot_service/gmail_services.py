import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import date, datetime
from apiclient import errors
from datetime import datetime


def connect_gmail():
     SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
     creds = None
     
     if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
     # If there are no (valid) credentials available, let the user log in.
     if not creds or not creds.valid:
          if creds and creds.expired and creds.refresh_token:
               creds.refresh(Request())
          else:
               print(os.getcwd())
               flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
               creds = flow.run_local_server(port=0)
          # Save the credentials for the next run
          with open('token.pickle', 'wb') as token:
               pickle.dump(creds, token)
     
     service = build('gmail', 'v1', credentials=creds)
     return service


def mark_as_read(service,msg_id):
     try:
          message = service.users().messages().modify(userId='me', id=msg_id,
                                                      body={'removeLabelIds': ['UNREAD']}).execute()
          # return message
     except errors.HttpError as error:
          print('An error occurred: %s' % error)
          

def check_message_validity(message):
     '''     validity = False
          if (message['snippet'].strip()==''):
               validity = True'''
     validity = True
     return validity
     
     
def get_relevant_emails(service):
     # Call the Gmail API to fetch INBOX
     results = service.users().messages().list(userId='me',labelIds = ['UNREAD']).execute()
     unread_messages = results.get('messages', [])
     # Select relevant messages
     selected_messages = []
     for message in unread_messages:
          msg = service.users().messages().get(userId='me', id=message['id']).execute()
          mark_as_read(service,message['id'])
          validity = check_message_validity(message)
          if (validity == True):
               selected_messages.append(msg)
     return selected_messages


def get_info_from_mail(selected_messages):
     # Fetch out emailID, subject etc.
     date_today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     final_list = []
     for message in selected_messages:
          headers = message['payload']['headers'] # list
          required_stuff = {} # name, subject, email, gender
          subject = None
          email = None
          gender = 'M'
          gender_list = ['M','F']
          for item in headers:
               if (item['name']=='From'):
                    name = item['value'].split('<')[0].strip()
                    email = item['value'].split('<')[1].split('>')[0]
               elif(item['name']=='Subject'):
                    info = item['value']
                    # case 1 - correct info
                    # case 2 - incorrect info
                    # case 3 - missing info
                    lst = info.split(']')
                    if(len(lst)==2): # correct flow
                         gender = lst[0][-1].upper()
                         print('[Gm-serv]',gender)
                         if(gender not in gender_list):
                              print("[Gm-serv]incorrect gender")
                              gender = 'M'

                    # subject = item['value']
                         subject = lst[1]
                    
                    print('[mail-bot] :: Request recieved :: ',subject)
                    flag = True
          if(subject and email and flag):
               required_stuff['request_date'] = date_today
               required_stuff['shoe_names'] = subject
               required_stuff['subscriber_id'] = email
               required_stuff['gender'] = gender
               final_list.append(required_stuff)
               print('[Gm-serv] appended info list')
               flag = False
     return final_list
# TODO some unsubscribe logic in the same loop


