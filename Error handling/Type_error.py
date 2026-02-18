try:
  a = 5
  b = "hello"
  c = a + b
except TypeError:
  print("You can't add a number and a string.")
else:
  print(f"The result is {c}")