import time
from plyer import notification
from playsound import playsound
from threading import Thread
 
def music():
    playsound(r"/home/vivek/Desktop/Javascript Projects/python-intresting-program/notifier/uncle.mp3")


def notify(): 
    notification.notify(
        title = "Drink Water",
        message="Stay Hydrated" ,
        app_name="Health Notifier",
        app_icon=r"/home/vivek/Desktop/Javascript Projects/python-intresting-program/notifier/drink-water.ico",
        # displaying time
        timeout=15,
        toast=False
    )

while True:
    t2=Thread(target=notify)
    t1=Thread(target=music)
    t2.start()
    t1.start()


    # waiting time
    time.sleep(20*60)

# $ pythonw.exe .\notifier.py  
# that it run in window 

# pyinstaller --onefile --hidden-import plyer.platforms.linux.notification filename.py 