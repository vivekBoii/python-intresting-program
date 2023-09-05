import random

lst=[0,1,2]
weapon=["Snake","Water","Gun"]
outcome=[[0,1,-1],[-1,0,1],[1,-1,0]]
print("Enter to game of Snake Water and Gun")
while(True):
    inp=int(input("Type 1 to play\nType 0 to exit\n"))
    if(inp==1):
        print("It have 10 Rounds")
        point=0
        for i in range(1,11):
            print(f"Round {i}:")
            choice=int(input("Type 0 to choose snake\nType 1 to choose Water\nType 2 to choose Gun\n"))
            comp=random.choice(lst)
            if(outcome[choice][comp]==0):
                print(f"It's a Draw Computer choose {weapon[comp]}\nPoints are : {point}")
            elif(outcome[choice][comp]==-1):
                print(f"You lose Computer choose {weapon[comp]}\nPoints are : {point}")  
            else:
                point=point+1
                print(f"You won Computer choose {weapon[comp]}\nPoints are : {point}") 
        if(point==5):
            print("Game is Draw")
        elif(point>5):
            print("You won Game")
        else:
            print("You lose Game")

    else:
        print("Thank You")
        break
