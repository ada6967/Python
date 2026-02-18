first=int(input("Enter the first number:"))
second=int(input("Enter the second number:"))

try:
    total=first/second
    print(total)
except:
    print("You put 0 for the second number but nothing can be divisible by it so try again.")