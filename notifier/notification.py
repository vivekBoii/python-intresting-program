import time
from plyer import notification
from playsound import playsound
from threading import Thread
 
def music():
    playsound(r"C:\Users\yadav\OneDrive\Desktop\vivek\notifier\uncle.mp3")


def notify(): 
    notification.notify(
        title = "Drink Water",
        message="Stay Hydrated" ,
        app_name="Health Notifier",
        app_icon=r"C:\Users\yadav\OneDrive\Desktop\vivek\notifier\drink-water.ico",
        # displaying time
        timeout=15,
        toast=False
    )

t1=Thread(target=music)
t1.start()

t2=Thread(target=notify)
t2.start()

# waiting time
time.sleep(60*60)

# $ pythonw.exe .\notifier.py  
# that it run in window 