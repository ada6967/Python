first=int(input("Enter your first number:"))
second=int(input("Enter your second number:"))

try:
  result=first/second

except ZeroDivisionError:
  print("You put 0 for the second number but nothing can be divisible by it so try again.")

else:
  print(f"The result is {result}")