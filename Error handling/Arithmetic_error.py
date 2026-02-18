try:
  import math
  num = -4
  result = math.sqrt(num)
except ValueError:
  print("Cannot find square root of negative number.")
else:
  print(result)