import win32com.client

speaker=win32com.client.Dispatch("SAPI.Spvoice")

while(True):
    s=input("Enter the input to Be Spoken\n")
    speaker.speak(s)
    check=input("press 0 to Exit or Press any Key to continue")
    if(check==0):
        break
    else:
        continue

# jai shreee raam