import requests
import json
import pyttsx3

response=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=ec946773bf264300b09a6c35fc51715a")

# beautify
# obj=json.loads(response.text)

# json_formatted_str = json.dumps(obj, indent=4)
# print(json_formatted_str)

title_lst=[]

json_data=response.json()
if json_data and 'articles' in json_data:
    for content in json_data['articles']:
        title = content.get('title')
        title_lst.append(title)

engine=pyttsx3.init()
voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('rate',150)
engine.setProperty('volume',.1)
engine.setProperty('voice',voice_id)

for index,name in enumerate(title_lst,start=1):
    print(str(index) +")."+name)
    engine.say(name)
    engine.runAndWait()

# voices = engine.getProperty('voices')
  
# for voice in voices: 
#     print("Voice:")
#     print("ID: %s" %voice.id)
#     print("Name: %s" %voice.name)
#     print("Age: %s" %voice.age)
#     print("Gender: %s" %voice.gender)
#     print("Languages Known: %s" %voice.languages)