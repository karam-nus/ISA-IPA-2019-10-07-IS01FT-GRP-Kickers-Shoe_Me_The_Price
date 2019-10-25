from __future__ import print_function
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import date
from apiclient import errors

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
          

def get_relevant_emails(service):
     # Call the Gmail API to fetch INBOX
     results = service.users().messages().list(userId='me',labelIds = ['UNREAD']).execute()
     unread_messages = results.get('messages', [])
     # Select relevant messages
     selected_messages = []
     for message in unread_messages:
          msg = service.users().messages().get(userId='me', id=message['id']).execute()
          mark_as_read(service,message['id'])
          if (msg['snippet'].strip()==''):
               selected_messages.append(msg)
     return selected_messages

def get_info_from_mail(selected_messages):
     # Fetch out emailID, subject etc.
     date_today = date.today()
     final_list = []
     for message in selected_messages:
          headers = message['payload']['headers'] # list
          required_stuff = {} # name, subject, email
          subject = None
          email = None
          for item in headers:
               if (item['name']=='From'):
                    name = item['value'].split('<')[0].strip()
                    email = item['value'].split('<')[1].split('>')[0]
               elif(item['name']=='Subject'):
                    subject = item['value']
                    print('[mail-bot] :: Request recieved :: '+subject)
                    flag = True
          if(subject and email and flag):
               required_stuff['request_date'] = date_today
               required_stuff['shoe_names'] = subject
               required_stuff['subscriber_id'] = email
               final_list.append(required_stuff)
               flag = False
     return final_list
# TODO some unsubscribe logic in the same loop


