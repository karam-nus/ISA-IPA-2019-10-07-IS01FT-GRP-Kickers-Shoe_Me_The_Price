from __future__ import print_function
import pickle
import os.path
import os
import time
import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import date
from apiclient import errors
from email.mime.text import MIMEText

def connect_gmail_send():
     SCOPES = ['https://www.googleapis.com/auth/gmail.compose']
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
     # print("Connection with gmail established")
     return service

def create_message( to, subject, message_text):
  message = MIMEText(message_text,'html')
  message['to'] = to
  # message['from'] = sender
  message['subject'] = subject
  # print(type(message))
  # print(type(message.as_string()))
  # print(type(message.as_bytes()))
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, message):
     '''Sends an email message.
     Arguments:
     service: an authorized Gmail API service instance.
     user_id: User's email address. To indicate the authenticated user, the special value "me" can be used.
     message: Message to be sent.'''

     try:
          print([push_mail] +time.ctime()+"{sending message}")
          message = service.users().messages().send(userId='me', body=message).execute()
          # print('Message Id: %s' % message['id'])
          # return message
     except (errors.HttpError) as error:
          print('an unexpected error occured while sending gmail message:') # +error)
def main():
     
     to='karamjotsingh@me.com'
     subject='Yo'
     send_message(connect_gmail_send(),create_message(to,subject,mail_body))
if __name__ == '__main__':
     main()
     