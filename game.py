import random
continue_game = "Y"
while continue_game.upper()== "Y":
  
    print("------------------------")
    print("------------------------")
    print("ROCK PAPER SCISSORS GAME")
    print("------------------------")
    print("------------------------")
    print("Choose your move")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    try:
       user_choice = int(input("Enter your choice(1-3) :"))
    except ValueError:
        print("Please enter numbers only")
        exit()

    match user_choice:
      case 1:
       user_choice="Rock"
      case 2:
        user_choice="Paper"
      case 3:
       user_choice="Scissors"
      case _:
       print("Invalid input case")

       exit()
 
    print("User choice is :",user_choice)

    computer_choice = random.randint(1,3)

    match computer_choice:
     case 1:
      computer_choice="Rock"
     case 2:
      computer_choice="Paper"
     case 3:
       computer_choice="Scissors"
     case _:
      print("Invalid input case")
      exit()
    print("Computer's choice is :",computer_choice)


    if user_choice==computer_choice:
      print("It's a tie")
    elif user_choice=="Rock" and computer_choice=="Scissors":
      print("You win")
    elif user_choice=="Paper" and computer_choice=="Rock":
       print("You win")
    elif user_choice=="Scissors" and computer_choice=="Paper":
      print("You win")
    else:
     print("Computer wins")
    continue_game=input("Do you want to continue? (Y/N): ")
print("Thankyou for playing")