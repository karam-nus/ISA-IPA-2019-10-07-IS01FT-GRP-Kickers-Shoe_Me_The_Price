import threading
import time
import mailbot_service.mailbot_controller as gfc
import send_mail
#import app

def worker(functionality,db_connection):
     n = 0
     if functionality == 'website-bot':
        while True:
               print("[website-bot] "+time.ctime() + "||listening||")
               
               import app
               
               time.sleep(90)
     elif functionality == 'mail-bot':
          while True:
               print("[mail-bot] "+time.ctime() + "||listening||")
               try:
                    gfc.execute_gmail_fetch(db_connection)
               except:
                    pass
               time.sleep(5)
     elif functionality == 'chat-bot':
        while True:
             print("[chat-bot]")
             time.sleep(90)
      # elif functionality == 'daily-updates':
      #   while True:
      #     print("[daily-updates]")
      #     time.sleep(10)

# if __name__ == '__main__':
def execute_processes(db_connection):
   functionality = ["website-bot", "mail-bot","chat-bot","daily-updates"]
   for i in functionality:
        threading.Thread(target=worker, args=(i,db_connection)).start()

