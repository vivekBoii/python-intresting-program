import pyttsx3

shoutout=["vivek","Jai shree raam"]

engine=pyttsx3.init()

for name in shoutout:
    engine.say(name)
    engine.runAndWait()