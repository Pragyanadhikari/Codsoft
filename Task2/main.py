import os
import math
def add():
    a, b = map(int, input("\nEnter your number in form of a+b: ").split(','))
    
    sum=a+b
    print("The addition is : ", sum)

def subtract():
    a, b = map(int, input("\nEnter your number in form of a-b: ").split(','))
    diff=a-b
    print("The difference is : ", diff)

def multiply():
    a, b = map(int, input("\nEnter your number in form of a*b: ").split(','))
    mul=a*b
    print("The multiplication is : ", mul)

def divide ():
    a, b = map(int, input("\nEnter your number in form of a/b: ").split(','))
    div=a/b
    print("The division is : ", div)

def powerFunction():
    a, b = map(int, input("\nEnter your number in form of a^b: ").split(','))
    power= a**b
    print("The power is : ", power)

def sqroot():
    a=int(input("\n Enter your number to find square root :"))
    squareroot = math.sqrt(a)
    print("The addition is : ", squareroot)

def main():
    os.system('clear')
    while True:
        print("\n\n=========Calculator=========\n\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit\n")

        userChoice=int(input("Enter your choice:"))
        if userChoice==1:
            add()
        elif userChoice==2:
            subtract()
        elif userChoice==3:
            multiply()
        elif userChoice==4:
            divide()
        elif userChoice==5:
            powerFunction()
        elif userChoice==6:
            sqroot()
        elif userChoice==7:
            exit()
        else:
            print("\nInvalid Choice.")

if __name__=="__main__":
    main()