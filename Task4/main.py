import os
import random
import string


userScore =0
computerScore =0

options= ("Rock","Paper","Scissors")

def computerChoice():
    computer=random.choice(options)
    return computer



def askUser():
    try:
        
        userChoice=int(input("Enter your choice:\n1.Rock\n2.Paper\n3.Scissors\n"))
    except ValueError:
        userChoice=-1
    return userChoice




def showscore():
    print("================================================")
    print(f"Your Score:{userScore}")
    print(f"Computer Score:{computerScore}\n\n")



def main():
    global userScore
    global computerScore
    ask=True
    
    os.system('clear')
    while ask:
        User =-1
        while User not in (1,2,3):
            User=askUser()
            if User== 1:
                userGuess= "Rock"
            elif User==2 :
                userGuess ="Paper"
            elif User == 3:
                userGuess ="Scissors"
            else:
                print("Wrong Choice")
                os.system('clear')
                
            
            computer=computerChoice()
            print(f"\nplayer:{userGuess}")
            print(f"Computer:{computer}")   

            if  userGuess == computer :
                print("It is tie!")
            elif userGuess == "Paper" and computer=="Rock":
                userScore +=1
            elif userGuess== "Paper" and computer=="Scissors":
                computerScore+=1
            elif userGuess=="Rock" and computer=="Paper":
                computerScore+=1
            elif userGuess =="Rock" and computer=="Scissors":
                userScore +=1
            elif userGuess=="Scissors" and computer=="Paper":
                userScore+=1
            elif userGuess=="Scissors" and computer =="Rock":
                computerScore+=1
        
        showscore()

        choice=input("\nDo you want to continue?(y/n):")
        if choice.lower()=="n" or choice.lower()=="no":
            ask=False
            os.system('clear')
        else: 
            os.system('clear')

if __name__=="__main__":
    main()