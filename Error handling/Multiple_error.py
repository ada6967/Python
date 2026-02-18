try:
  first=int(input("Enter the first number:"))
  second=int(input("Enter the second number:"))
  result=first/second
except ZeroDivisionError:
   print("You put 0 for the second number but nothing can be divisible by it so try again.")
except ValueError:
  print("You entered something that cannot be divisible.")
else:
  print(f"The result is {result}")