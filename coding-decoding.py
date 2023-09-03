import random
import string

ans=int(input("Type 1 to encode message\nType 2 to decode message\nType 0 to exit\n"))
while(ans==1 or ans==2):
    if(ans==1):
        mes=input("Enter your message\n")
        lst=mes.split(" ")
        mes=""
        if isinstance(lst, list):
            for i in lst:
                if(len(i)<=3):
                    i=i[::-1]
                else:
                    num=len(i)
                    ch=i[0]
                    i=i[1:]+ch
                    res = ''.join(random.choices(string.ascii_lowercase ,k=3))
                    i=res+i+res
                mes=mes+" "+i
        print("Your coded message is"+mes)

    else:   
        mes=input("Enter message to be decoded\n")
        lst=mes.split(" ")
        mes=""
        if isinstance(lst, list):
            for i in lst:
                if(len(i)<=3):
                    i=i[::-1]
                else:
                    num=len(i)
                    cha=i[num-4]
                    ch=i[3:num-4]
                    i=cha+ch
                mes=mes+" "+i
        print("Your decoded message is "+mes)
    ans=int(input("Type 1 to encode message\nType 2 to decode message\nType 0 to exit\n"))
else:
    print("Thank you")
