import requests
import pyttsx3

city=input("Enter the name of city\n")
file=requests.get(f"http://api.weatherapi.com/v1/current.json?key=381f85aeffd04ad6b41105812230509&q={city}&aqi=no")

file_json=file.json()
if file.json() and 'current' in file_json:
    temp=file_json['current'].get('temp_c')
    cond=file_json['current']['condition'].get('text')

report=f"The current temperature of {city} is {temp} and {cond}"

engine=pyttsx3.init()
engine.setProperty('rate',150)
engine.say(report)
engine.runAndWait()