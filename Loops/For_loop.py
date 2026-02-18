#Example 1 -  print numbers from 1 to 5
for i in range(1,6):
  print(i)
print()

#Example 2 - print numbers from 0 to 10
for i in range(0,11):
  print(i)
print()

#Example 3 - print each fruit in a list
fruits=["Watermelon", "Papaya", "Apple"]
for i in fruits:
  print(i)
print()

#Example 4 - print each vegetable in a list
vegetables=["Carrot", "Cucumber", "Onion"]
for i in vegetables:
  print(i)
print()

#Example 5 - print each charater in a word
greeting="hello"
for i in greeting:
  print(i)
print()

for i in "hello":
  print(i);
print()

#Example 6 - print even numbers 0 to 10
for i in range(0,10,2):
  print(i)
print()

for i in range(0,10,3):
  print(i)

for i in range(1,12,2):
  print(i)

#Example 7 - using for loop with a condition
numbers=[1, 2, 3, 4, 5, 6]
for i in numbers:
  if i % 2 == 0:
    print(i, "is even")
print()

#Example 8 - loop through a list with index numbers
color=["red", "orange", "yellow"]
for i in range(len(color)):
  print(i, color[i])