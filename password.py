print("PASSWORD GENERATOR")
print("------------------")
import random
import string
try:
  length=int(input("How many characters do you want in your password :"))
  if length <= 0:
       print("Password length must be greater than zero")
  else:
     print("1.Easy(letters only)")
     print("2.Medium(letter and numbers)")
     print("3.Strong(letter,numbers and special characters)")
     choice=int(input("Select password type(1-3) :"))
     letter = ""
     match choice:
          case 1:
            for i in range(length):
                  letter+=random.choice(string.ascii_letters)
         
          case 2:
           for i in range(length):
            letter+=random.choice(string.ascii_letters+string.digits)

          case 3:
           for i in range(length):
            letter+=random.choice(string.ascii_letters+string.digits+string.punctuation)
          case _:
           print("Invalid choice. Please select 1,2 or 3 as your choice")

     if letter != "":
            print("Generated Password :",letter)
except ValueError:
     print("Please enter numbers only")      
     
    