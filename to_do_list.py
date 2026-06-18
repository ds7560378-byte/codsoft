print("----------")
print("----------")
print("TO-DO LIST")
print("----------")
print("----------")
list=[]
while True:
     
    print("Choose a task to perform")
    print("1.Add task to list")
    print("2.View task from list")
    print("3.Update into list")
    print("4.Exit")
    try:
        choice=int(input("Enter your choice(1-4) :"))
    except ValueError:
        print("Please enter numbers only")
        continue

    match choice:
        case 1:
            n=int(input("How many tasks do you want to add :"))
            for i in range(n):
                a=input("Enter your task :")
                list.append(a)
            print("\nTasks added successfully.")
            print("\nCurrent Tasks :",list)
        case 2:
            if len(list)==0:
                print("No tasks available")
            else:
                print("Your tasks :")
                for i in range(len(list)):
                    print(i+1,  "." , list[i])
        case 3:
            if len(list)==0:
                print("No tasks available to update")
            else:
                print("Current Tasks :")
            
                for i in range(len(list)):
                    print(f"{i+1}.{list[i]}")
                   
                    try:
                        index=int(input("Enter task number to update :"))
                        if 1<=index <=len(list):
                            new_task=input("Enter updated tasks :")
                            list[index-1]=new_task
                            print("Task updated successfully")
                            print("Updated task:",list)
                        else:
                            print("Invalid task number")
                    except ValueError:
                        print("Please enter a valid number")
        case 4:
            print("Thankyou for using To-Do List.")
            break
        case _:
             print("Invalid choice,please enter 1,2,3,or 4 as your choice.")
    
