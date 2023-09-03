inp=input("Welcome to KBC , I will ask you simple question , there are seven stage , and no lifeline \nDo you want to start the game\nType Y/N\n")

if(inp=="Y" or inp=="y"):
    lst=[["What is Capital of India?","delhi"],
     ["How many states are ther in India","28"],
     ["The Constitution of India adopted Fundamental Duties from the Constitution of","russia"],
     ["At present how many Fundamental Duties are in the Constitution of India?","11"],
     ["National Bird","peacock"],
     ["National animal","tiger"],
     ["National Tree","banyan"],
     ]
    amount=[0,1000,10000,50000,"1 lakh","5 lakh","10 lakh","50 lakh"]
    index=0
    for i in range(7):
        print(lst[i][0])
        ans=input("Type your answer\n")
        if(ans.lower()==lst[i][1]):
            index=index+1
            print("You Won :"+str(amount[index]));
        else:
            print("You Lose and Won only rupee "+ str(amount[index]))
            break  
else:
    print("As you Wish")
print("Game is finished")  