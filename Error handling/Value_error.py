try:
  first=int(input("Enter the first number:"))
  second=int(input("Enter the second number:"))
  result = first/second
except ValueError:
  print("You entered something that cannot be divisible.")
else:
  print(f"The result is {result}")