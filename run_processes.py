import threading
import time
import mailer_service.mail_bot_controller as gfc

def worker(functionality,db_connection):
   if functionality == 'website-bot':
        while True:
             print("[website-bot]")
             time.sleep(90)
   elif functionality == 'mail-bot':
        while True:
             print("[mail-bot]")
             gfc.execute_gmail_fetch(db_connection)
             time.sleep(5)
   elif functionality == 'chat-bot':
        while True:
             print("[chat-bot]")
             time.sleep(90)

# if __name__ == '__main__':
def execute_processes(db_connection):
   functionality = ["website-bot", "mail-bot","chat-bot"]
   for i in functionality:
        threading.Thread(target=worker, args=(i,db_connection)).start()

