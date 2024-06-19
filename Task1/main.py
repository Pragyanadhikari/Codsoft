import os
from colorama import Back,Fore
from rich.console import Console

tasks=[]

def assign():
    n_task=int(input("\nHow many task you want to add?"))
    for i in range(n_task):
        task=input("\nEnter your task:")
        tasks.append({"task": task, "done": False})
        print(Fore.CYAN+"Task added\n"+Fore.RESET)

def showtask():
    print("\n"+Back.LIGHTCYAN_EX+"The available task are:"+Back.RESET)
    for index,task in enumerate(tasks):
        status="Done" if task["done"] else "Not Done"
        print(f"{index+1}.{task['task']} - {status}")


def marktask():
    task_index=int(input("\nEnter task number you want to mark as done:\n")) - 1
    if 0<=task_index<len(tasks):
        tasks[task_index]["done"]=True
        print(Fore.CYAN+"Task marked as done.\n"+Fore.RESET)
    else:
        print(Fore.CYAN+"Invalid Taks number.\n"+Fore.RESET)


def main():
    os.system('clear')
    while True:
        print(Fore.RED+"\n==============TO-DO list================\n"+Fore.RESET)
        print(Fore.LIGHTBLUE_EX+"1. Enter task."+Fore.RESET)
        print(Fore.LIGHTBLUE_EX+"2. View Task."+Fore.RESET)
        print(Fore.LIGHTBLUE_EX+"3. Mark as done"+Fore.RESET)
        print(Fore.LIGHTBLUE_EX+"4. Exit."+Fore.RESET)

        userChoice=int(input("\n"+Back.LIGHTGREEN_EX+"Your choice:"+Back.RESET+"\n"))

        if userChoice == 1:
           assign()
        elif userChoice == 2:
            showtask()
        elif userChoice == 3:
            marktask()
        elif userChoice==4:
           exit()
        else:
            os.system('clear')
            print("Invalid Choice.")
            

if __name__=="__main__":
    main()





