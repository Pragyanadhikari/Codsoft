
import os

def addContact():
    name=input("Enter your name:")
    address=input("Enter your address:")
    phonenumber=input("Enter your phone number:")
    email=input("Enter your email:")
    with open('contacts.txt','a') as file:
        file.write(f"{name},{address},{phonenumber},{email}")
    print("Contact Added Successfully.")
def ViewContact():
    try:
        with open('contacts.txt', 'r') as file:
            contacts = file.readlines()
            if contacts:
                print("Contacts:")
                for contact in contacts:
                    print(contact.strip())
            else:
                print("No contacts found.")
    except FileNotFoundError:
        print("No contacts found.")
def SearchContact():
    search_query = input("Enter name or number to search: ").lower()

    try:
        with open('contacts.txt', 'r') as file:
            contacts = file.readlines()
            matching_contacts = []

            for contact in contacts:
                if search_query in contact.lower():
                    matching_contacts.append(contact.strip())  
            if matching_contacts:
                print("Matching contacts:")
                for matching_contact in matching_contacts:
                    print(matching_contact)
            else:
                print("No matching contacts found.")
    except FileNotFoundError:
        print("No contacts found.")
def UpdateContact():
    search_query = input("Enter name or number to search for the contact you want to update: ").lower()
    try:
        with open('contacts.txt', 'r') as file:
            contacts = file.readlines()
        matching_contacts = []
        for contact in contacts:
            if search_query in contact.lower():
                matching_contacts.append(contact.strip())  

        if matching_contacts:
            print("Matching contacts:")
            for idx, matching_contact in enumerate(matching_contacts):
                print(f"{idx + 1}. {matching_contact}")

            selection = int(input("Enter the number corresponding to the contact you want to update: ")) - 1
            if selection >= 0 and selection < len(matching_contacts):
                old_contact = matching_contacts[selection].split(',')
                new_name = input("Enter new name: ")
                new_address = input("Enter new address: ")
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email address: ")
 
                updated_contact = ','.join([new_name,new_address, new_phone, new_email]) + '\n'
                contacts[contacts.index(matching_contacts[selection])] = updated_contact

                with open('contacts.txt', 'w') as file:
                    file.writelines(contacts)

                print("Contact updated successfully.")
            else:
                print("Invalid selection.")
        else:
            print("No matching contacts found.")
    except FileNotFoundError:
        print("No contacts found.")
def DeleteContact():
    search_query = input("Enter name or number to search for the contact you want to delete: ").lower()

    try:
        
        with open('contacts.txt', 'r') as file:
            contacts = file.readlines()

       
        matching_contacts = []

        
        for contact in contacts:
            
            if search_query in contact.lower():
                matching_contacts.append(contact.strip())  

        if matching_contacts:
            print("Matching contacts:")
            for idx, matching_contact in enumerate(matching_contacts):
                print(f"{idx + 1}. {matching_contact}")

            
            selection = int(input("Enter the number corresponding to the contact you want to delete: ")) - 1
            if selection >= 0 and selection < len(matching_contacts):
                
                contacts.remove(matching_contacts[selection] + '\n')

                
                with open('contacts.txt', 'w') as file:
                    file.writelines(contacts)

                print("Contact deleted successfully.")
            else:
                print("Invalid selection.")
        else:
            print("No matching contacts found.")
    except FileNotFoundError:
        print("No contacts found.")



def choice():
    print("Enter your choice:\n1.Add Contact\n2.View Contact\n3.Search Contact\n4.Update Contact\n5.Delete Contact")
    
    try :
        selected=int(input())
    except  ValueError:
        selected=-1
    return selected

def main():
    ask=True
    while ask:

        variable=-1
        while variable not in (1,2,3,4,5):
            variable=choice()
            if variable==1:
                addContact()
            elif variable==2 :
                ViewContact()
            elif variable ==3:
                SearchContact()
            elif variable==4:
                UpdateContact()
            elif variable==5:
                DeleteContact()
            else:
                print("Wrong Choice")

if __name__=="__main__":
    main()