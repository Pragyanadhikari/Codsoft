import string
import random
import os

def main():
    choice=[]
    choice1=string.ascii_letters
    choice2=string.digits
    choice3=string.punctuation
    Passlength=int(input("Enter length of password to you want to generate:"))
    choice.extend(choice1)
    choice.extend(choice2)
    choice.extend(choice3)
    random.shuffle(choice)
    print("\nYour Password is:")
    print("".join(random.sample(choice,Passlength)))



if __name__=="__main__":
    os.system('clear')
    main()