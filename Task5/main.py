
import os

def addContact():
    name=input("\nEnter your name:")
    address=input("Enter your address:")
    phonenumber=input("Enter your phone number:")
    email=input("Enter your email:")
    with open('contacts.txt','a') as file:
        file.write(f"{name},{address},{phonenumber},{email}\n")
    print("\nContact Added Successfully.\n")


def ViewContact():
    try:
        with open('contacts.txt', 'r') as file:
            contacts = file.readlines()
            if contacts:
                print("\nContacts:\n")
                print(f"{'S.no':<5}{'Name':<20}{'Address':<30}{'Phone Number':<15}{'Email'}")
                for idx, contact in enumerate(contacts):
                    contact_details = contact.strip().split(',')
                    if len(contact_details) >= 4:
                        print(f"{idx + 1:<5}{contact_details[0]:<20}{contact_details[1]:<30}{contact_details[2]:<15}{contact_details[3]}")
                    else:
                        print(f"Contact at line {idx + 1} does not have complete details.")
            else:
                print("No contacts found.")
    except FileNotFoundError:
        print("No contacts found.")



        
def SearchContact():
    search_query = input("\nEnter name or number to search: ").lower()

    try:
        with open('contacts.txt', 'r') as file:
            contacts = file.readlines()
            matching_contacts = []

            for contact in contacts:
                if search_query in contact.lower():
                    matching_contacts.append(contact.strip())  
            if matching_contacts:
                print("\nMatching contacts:\n")
                for matching_contact in matching_contacts:
                    print(matching_contact)
            else:
                print("\nNo matching contacts found.")
    except FileNotFoundError:
        print("\nNo contacts found.")

def UpdateContact():
    def get_contacts():
        try:
            with open('contacts.txt', 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print("\nNo contacts found.")
            return []

    def display_matching_contacts(contacts, query):
        matching = [contact.strip() for contact in contacts if query in contact.lower()]
        if matching:
            print("\nMatching contacts:\n")
            for idx, contact in enumerate(matching):
                print(f"{idx + 1}. {contact}")
        return matching

    def get_contact_details():
        new_name = input("\nEnter new name: ").strip()
        new_address = input("Enter new address: ").strip()
        new_phone = input("Enter new phone number: ").strip()
        new_email = input("Enter new email address: ").strip()
        return [new_name, new_address, new_phone, new_email]

    def update_contact_in_file(contacts, old_contact, new_details):
        updated_contact = ','.join(new_details) + '\n'
        index = contacts.index(old_contact + '\n')
        contacts[index] = updated_contact
        with open('contacts.txt', 'w') as file:
            file.writelines(contacts)

    search_query = input("\nEnter name or number to search for the contact you want to update: ").lower()
    contacts = get_contacts()
    if not contacts:
        return

    matching_contacts = display_matching_contacts(contacts, search_query)
    if not matching_contacts:
        print("\nNo matching contacts found.")
        return

    try:
        selection = int(input("Enter the number corresponding to the contact you want to update: ")) - 1
        if 0 <= selection < len(matching_contacts):
            old_contact = matching_contacts[selection]
            new_details = get_contact_details()
            if all(new_details):
                update_contact_in_file(contacts, old_contact, new_details)
                print("Contact updated successfully.")
            else:
                print("All fields are required. Update failed.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def DeleteContact():
    search_query = input("\nEnter name or number to search for the contact you want to delete: ").lower()

    try:
        
        with open('contacts.txt', 'r') as file:
            contacts = file.readlines()

       
        matching_contacts = []

        
        for contact in contacts:
            
            if search_query in contact.lower():
                matching_contacts.append(contact.strip())  

        if matching_contacts:
            print("\nMatching contacts:")
            for idx, matching_contact in enumerate(matching_contacts):
                print(f"{idx + 1}. {matching_contact}")

            
            selection = int(input("\nEnter the number corresponding to the contact you want to delete: ")) - 1
            if selection >= 0 and selection < len(matching_contacts):
                
                contacts.remove(matching_contacts[selection] + '\n')

                
                with open('contacts.txt', 'w') as file:
                    file.writelines(contacts)

                print("\nContact deleted successfully.")
            else:
                print("\nInvalid selection.")
        else:
            print("\nNo matching contacts found.")
    except FileNotFoundError:
        print("No contacts found.")



def choice():
    print("Enter your choice:\n1.Add Contact\n2.View Contact\n3.Search Contact\n4.Update Contact\n5.Delete Contact\n6.Exit")
    
    try :
        selected=int(input())
    except  ValueError:
        selected=-1
    return selected

def main():
    ask=True
    while ask:

        variable=-1
        while variable not in (1,2,3,4,5,6):
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
            elif variable==6:
                exit()
            else:
                print("Wrong Choice")

if __name__=="__main__":
    main()