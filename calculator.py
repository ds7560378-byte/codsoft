print("ADVANCED CALCULATOR")
print("-------------------")
print("-------------------")

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Power")
print("6.Factorial")
print("7.Modulus")
choice=int(input("Select an operation to perform (1-7) :"))

result=0
outcome=1
fact=1
n=int(input("How many numbers do you want to use? :"))

match choice:
  case 1:
    for i in range(n):
      a=float(input("Enter a number :"))
      result=result+a
    
  case 2:
    result=float(input("Enter the first number :"))
    for i in range(n-1):
        a=float(input("enter the next number :"))
        result=result-a
     
  case 3:
    for i in range(n):
     a=float(input("Enter a number :"))
     outcome=outcome*a
  case 4:
    try:
       if n != 2:
        print("Please enter only two numbers for division")
       else:
        result=float(input("Enter the first number :"))
        for i in range(n-1):
         a=float(input("Enter the second number :"))
         result=result/a
  
    except ZeroDivisionError:
      print("Number cannot be divisible by zero")
    except ValueError:
      print("Please provide a valid number for division")

  case 5:
    if n != 2:
      print("Please enter only two numbers for power operation")
    else:
      result=float(input("Enter the number(base number) :"))
      for i in range(n-1):
        a=float(input("Enter the power :"))
        result=result**a
   
  case 6:
    if n > 1:
     print("Factorial can be calculated for only one number")
    else:
      n=int(input("Enter the number for calculation :"))
      for i in range(1,n+1):
        fact=fact*i
        result=fact

  case 7:
    if n > 2:
      print("Please enter exactly two numbers for modulus calculation")
    else:
      result=float(input("Enter the first number :"))
      for i in range(n-1):
        a=float(input("Enter the second number :"))
        result=result%a
    
  case _:
      print("Invalid choice,please select a number from 1 to 7 as your choice.")

match choice:
  case 1:
    print(result)
  case 2:
    print(result)
  case 3:
    print(outcome)
  case 4:
    print(result)
  case 5:
    print(result)
  case 6:
    print(result)
  case 7:
    print(result)

