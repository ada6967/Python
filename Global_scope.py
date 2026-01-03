q=11  # q has a local scope and hence can be used outside the function
def number():
  print(q)

number()

print(q)