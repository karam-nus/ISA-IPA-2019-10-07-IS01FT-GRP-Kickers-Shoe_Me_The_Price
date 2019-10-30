import threading
import time
import mailbot_service.mailbot_controller as gfc
import send_mail
from send_mail import daily_script
from datetime import datetime
from persistence import db_updates as db
# import app


def worker(functionality, db_connection):
     n = 0
     if functionality == 'website-bot':
        while True:
             try:
                  import app
                  print("[website-bot] " + time.ctime() + " {listening}")

             except Exception as e:
                  print('[rp-wb]Exception in last request.\n', e)
                  pass
             time.sleep(5)
     elif functionality == 'mail-bot':
          while True:
               try:
                    gfc.execute_gmail_fetch(db_connection)
                    print("[mail-bot] " + time.ctime() + " {listening}")

               except Exception as e:
                    print('[rp-mb]Exception in last request.\n', e)
                    pass
               time.sleep(5)
     elif functionality == 'daily-updates':
        while True:
            t = datetime.now().strftime('%H:%M')
            print(t)
            if datetime.now().strftime('%H:%M') in ['07:00', '07:01', '07:02']:

              print("Time matched")
              daily_script.daily_updates(db_connection)

            daily_script.instant_updates(db_connection)

            print("[daily-updates]")
            time.sleep(5)


# if __name__ == '__main__':
def execute_processes(db_connection):
   functionality = ["website-bot", "mail-bot","daily-updates"]
   for i in functionality:
        threading.Thread(target=worker, args=(i,db_connection)).start()

