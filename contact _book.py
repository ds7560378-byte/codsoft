print("------------")
print("CONTACT BOOK")
print("------------")

contact={}

while True:
    print("Choose one operation ")
    print("1.Add Contacts")
    print("2.View Contacts")
    print("3.Search Contacts")
    print("4.Update Contact")
    print("5.Delete Contact")
    print("6.Exit Contact")  
    try:
        choice=int(input("Enter your choice :"))
    except ValueError:
        print("Please enter numbers only")
        continue
    match choice:
        case 1:
            
            name=input("Enter Name :").strip()
            if name == "":
                print("Name cannot be empty")
            elif name in contact:
                print("Contact already exists")
            else:
                phone=input("Enter contact number :").strip()
                if phone.isdigit() and len(phone) == 10:
                    contact[name] = phone
                    print("Contact added successfully")
                else:
                    print("Enter a valid phone number")
        case 2:
            if contact:
                print("\nAll contacts:")
                for name,phone in contact.items(): 
                    print(name, ":", phone)
            else:
                print("No contact available")
            
        case 3:
            name=input("Enter name to serach :")
            if name in contact:
                print(name, ":" ,contact[name])
            else:
                print("Contact not found")
        
        case 4:
            name=input("Enter name to update :").strip()
            if name in contact:
                new_phone=input("Enter updated contact number :").strip()
                if new_phone.isdigit() and len(new_phone) == 10:
                    contact[name]=new_phone
                    print("Contact updated successfully")
                    print(name ,":",contact[name])
                else:
                    print("Enter a valid number")
            else:
                print("contact not found")
              
        case 5:
            name=input("Enter name to delete contact :").strip()
            if name in contact:
                del contact[name]
                print("Deleted contact :",name)
            else:
                print("No contact found")
            
        case 6:
            print("Exiting contact book")
            break
        
        case _:
            print("Invalid choice,please enter a number between 1 and 6")
    

            
            

